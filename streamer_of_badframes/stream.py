#!/usr/bin/env python3

import cv2
import gi
import threading

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject, GLib


class SensorFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self, filesource, frame_size, _callback=None):
        super(SensorFactory, self).__init__()
        self.stop_server_callback = _callback

        self.cap = cv2.VideoCapture(filesource, 0)  # 2560 × 1920

        self.number_frames = 0

        self.frame_size = frame_size  # frame_size


        self.fps = 10
        self.duration = 1 / self.fps * Gst.SECOND  # duration of a frame in nanoseconds

        self.launch_string = 'appsrc name=source is-live=false block=true format=GST_FORMAT_TIME ' \
                             'caps=video/x-raw,format=BGR,width={0},height={1},framerate={2}/1 ' \
                             '! videoconvert ! video/x-raw,format=I420 ' \
                             '! x264enc speed-preset=ultrafast tune=zerolatency ' \
                             '! rtph264pay config-interval=1 name=pay0 pt=96'.format(self.frame_size[0],
                                                                                     self.frame_size[1], self.fps)
        self.last_frame = None
        print("Control parameters:")
        self.send_once_stop = bool(1)
        # print("self.frame_size" + self.frame_size.__str__())

    def on_need_data(self, src, lenght):
        self.send_once_stop = bool(1)
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, self.frame_size)
                data = frame.tostring()
                buf = Gst.Buffer.new_allocate(None, len(data), None)
                buf.fill(0, data)
                buf.duration = self.duration
                timestamp = self.number_frames * self.duration
                buf.pts = buf.dts = int(timestamp)
                buf.offset = timestamp
                self.number_frames += 1
                retval = src.emit('push-buffer', buf)
                # print('pushed buffer, frame {}, duration {} ns, durations {} s'.format(self.number_frames,
                #                                                                        self.duration,
                #                                                                        self.duration / Gst.SECOND))

                if retval != Gst.FlowReturn.OK:
                    print(retval)
            else:
                print("!!! Errors while loading the current frame: Test pause")
                print("ret: " + str(ret))
                print("Frame is empty!")

            if frame is None:
                print("Frame is Empty - stream ended.")
                if self.send_once_stop:
                    self.stop_server_callback()
                    # block repeated stop signal
                    self.send_once_stop = bool(0)

        else:
            # if self.stop_server_callback:
            # self.send_shutdown_to_tester()
            print("Send callback to TESTER! Test ended!")

    def do_create_element(self, url):
        return Gst.parse_launch(self.launch_string)

    def do_configure(self, rtsp_media):
        self.number_frames = 0
        appsrc = rtsp_media.get_element().get_child_by_name('source')
        appsrc.connect('need-data', self.on_need_data)


class GstServer(GstRtspServer.RTSPServer):
    def __init__(self, camera_streams, callback):
        super(GstServer, self).__init__()
        GObject.threads_init()
        Gst.init(None)
        self.set_service("8554")  # set port for rtsp translation
        self.factories = []

        # add multipoint for each factory
        for stream in camera_streams:
            stream_factory = SensorFactory(stream.filesource, stream.frame_size, callback)
            stream_factory.set_shared(True)
            self.get_mount_points().add_factory("/{}".format(stream.mountpoint), stream_factory)
            print("Mount point for factory: " + "/{}".format(stream.mountpoint))
            self.factories.append(stream_factory)

        self.attach(None)
        self.loop = None

        self.server_thread = threading.Thread(name='test-video-stream', target=self.server_thread)

    def start(self):
        self.server_thread.start()

    def stop(self):
        print("Stop server....")
        self.loop.quit()

    def server_thread(self, do_loop=False):
        print("RTSP Server thread started...")
        self.loop = GObject.MainLoop()
        self.loop.run()
        print("RTSP Server thread ended.")
