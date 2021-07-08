# import cv2
# import numpy as np
#
# # Create a VideoCapture object and read from input file
# # If the input is the camera, pass 0 instead of the video file name
# path_video_src = "/home/interceptor/Документы/Git_repo_telesoft/DATA/videot_3/fish8_qa.mp4"
#
# cap = cv2.VideoCapture(path_video_src)
#
# # Check if camera opened successfully
# if (cap.isOpened()== False):
#   print("Error opening video stream or file")
#
# # Read until video is completed
# while(cap.isOpened()):
#   # Capture frame-by-frame
#   ret, frame = cap.read()
#   if ret == True:
#
#     # Display the resulting frame
#     cv2.imshow('Frame',frame)
#
#     # Press Q on keyboard to  exit
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#       break
#
#   # Break the loop
#   else:
#     break
#
# # When everything done, release the video capture object
# cap.release()
#
# # Closes all the frames
# cv2.destroyAllWindows()


######################################################################################
from threading import Thread
import cv2, time

class ThreadedCamera(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        # FPS = 1/X
        # X = desired FPS
        self.FPS = 1/41
        self.FPS_MS = int(self.FPS * 1000)

        # Start frame retrieval thread
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(self.FPS)

    def show_frame(self):
        cv2.imshow('frame', self.frame)
        cv2.waitKey(self.FPS_MS)

if __name__ == '__main__':
    src = '/home/interceptor/Документы/Git_repo_telesoft/DATA/videot_3/fish8_qa.mp4'
    threaded_camera = ThreadedCamera(src)
    while True:
        try:
            threaded_camera.show_frame()
        except AttributeError:
            pass