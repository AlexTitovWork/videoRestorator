#!/usr/bin/env python3
import cv2

# path_video_src = "../resources/fish8_leave.mp4"
path_video_src = "/home/interceptor/Документы/Git_repo_telesoft/DATA/videot_3/fish8_qa.mp4"

# path_video_dst = "../resources/fish8_qa_restored.mp4"
path_video_dst = "/home/interceptor/Документы/Git_repo_telesoft/DATA/videot_3/fish8_tahoe.mp4"

def restrore_and_transcode(path_video_src, path_video_dst):
    capture = cv2.VideoCapture(path_video_src)
    # use codec H264 to restore video time duration lag in file.
    # https: // www.programcreek.com / python / example / 89348 / cv2.VideoWriter_fourcc
    fourCodec = cv2.VideoWriter_fourcc(*'H264')
    # out = cv2.VideoWriter(path_video_dst, fourCodec, 120.0, (1280, 1280))
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(path_video_dst, fourCodec, 10.0, (1280, 1280))

    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret == True:
            out.write(frame)
            print("Frame write:" + str(ret))
            cv2.imwrite('../resources/image.png', frame)
            # cv2.imshow('frame', frame)
            # choice = input("\033[1;32;40m Press 'Q' and then 'Enter' stop.\033[0m \n")
            # if choice == "Q" or choice == "q":
            #     break
        else:
            break  # Release all if complete
    capture.release()
    out.release()
    # cv2.destroyAllWindows()


restrore_and_transcode(path_video_src, path_video_dst)