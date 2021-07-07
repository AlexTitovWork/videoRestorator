#!/usr/bin/env python3
import cv2

# path_video_src = "../resources/fish8_leave.mp4"
# path_video_src = "/home/interceptor/Документы/Git_repo_telesoft/DATA/videot_3/fish8_qa.mp4"
path_video_src = "/home/interceptor/Документы/DATA/test5/fish4_1min.mp4"

# path_video_dst = "../resources/fish8_qa_restored.mp4"
# path_video_dst = "/home/interceptor/Документы/Git_repo_telesoft/DATA/videot_3/fish8_tahoe.mp4"
path_video_dst = "/home/interceptor/Документы/DATA/test5/fish4_1min_restoration.avi"

def restrore_and_transcode(path_video_src, path_video_dst):
    capture = cv2.VideoCapture(path_video_src)
    # use codec H264 to restore video time duration lag in file.
    # https: // www.programcreek.com / python / example / 89348 / cv2.VideoWriter_fourcc
    fourCodec = cv2.VideoWriter_fourcc(*'H264')
    # fourCodec = cv2.VideoWriter_fourcc(*'avc1')
    # fourCodec = cv2.VideoWriter_fourcc('h', '2', '6', '4')
    # out = cv2.VideoWriter(path_video_dst, fourCodec, 120.0, (1280, 1280))
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(path_video_dst, fourCodec, 10.0, (1280, 1280))

    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret == True:
            # print("Frame write:" + str(ret))
            cv2.imshow('frame', frame)
            out.write(frame)
        else:
            break  # Release all if complete

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    capture.release()
    out.release()
    # cv2.destroyAllWindows()


restrore_and_transcode(path_video_src, path_video_dst)