#!/usr/bin/env python3
import time
import requests
from stream import *

class cameras_strem(object):
    def __init__(self, filesource, mountpoint, frame_size):
        """Constructor"""
        self.filesource = filesource
        self.mountpoint = mountpoint
        self.frame_size = frame_size


    def send_shutdown_to_tester(self):
        print("Send: requests.post('http://localhost:5000/shutdown')")
        res = requests.post('http://localhost:5000/shutdown')
        # time.sleep(60*3)
        rtsp_server.stop()  # nonblocking

        if res.ok:
            print(res)

# starting RTSP server for showing results from chosen camera
print("\033[1;33;40m Starting RTSP server...\033[1;37;40m")


# Test5 DEBUG on old configuration with new clips
# ZONE3
## Gray sedan enter and get -off without park
# filesource1 = '../../../Git_repo_telesoft/DATA/videot_3/fish8_qa.mp4'
filesource1 = '../../../Git_repo_telesoft/DATA/videot_3/master2_qa.mp4'


# ZONE1
mountpoint1 = "camera1"

frame_size1 = (1280, 1280)  # frame_size 11

# ZONE1
cameras_streams_entrance = cameras_strem(filesource1, mountpoint1, frame_size1)

# ZONE1
cameras_streams = list()
cameras_streams.append(cameras_streams_entrance)

#######################################################################

rtsp_server = GstServer(cameras_streams, cameras_streams_entrance.send_shutdown_to_tester)

print("Start server....")
rtsp_server.start()  # nonblocking


