import cv2

path_video_src = "../"
path_video_dst = "../"


def restrore_and_transcode(path_video_src, path_video_destanation):
    capture = cv2.VideoCapture(path_video_src)
    # use codec H264 to restore video time duration lag in file.
    # https: // www.programcreek.com / python / example / 89348 / cv2.VideoWriter_fourcc
    fourCodec = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter(path_video_dst, fourCodec, 20.0, (1024, 512))
    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret == True:
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break  # Release all if complete
    capture.release()
    out.release()
    cv2.destroyAllWindows()
