
import cv2

# path_video_src = "/home/interceptor/Документы/Git_repo_telesoft/DATA/videot_3/fish8_qa.mp4"
path_video_src = "/home/interceptor/Документы/DATA/test5/fish4_1min.mp4"

# Write only in AVI format
path_video_dst = "/home/interceptor/Документы/DATA/test5/output.avi"


cap = cv2.VideoCapture(path_video_src)

# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the total numer of frames in the video.
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
frame_number = 0
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)  # optional
success, frame = cap.read()
# Writer
# fourCodec = cv2.VideoWriter_fourcc('h', '2', '6', '4')
# out = cv2.VideoWriter(path_video_dst, fourCodec, 10, (1280, 1280))
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(path_video_dst, fourcc, 10.0, (1280,  1280))

while success and frame_number <= frame_count:
    # do stuff

    frame_number += fps
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    success, frame = cap.read()

    if success:
        cv2.imshow("Video", frame)
        out.write(frame)
    else:
        break
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
out.release()