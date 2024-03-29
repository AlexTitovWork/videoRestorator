import cv2

# path_video_src = "/home/interceptor/Документы/Git_repo_telesoft/DATA/videot_3/fish8_qa.mp4"
path_video_src = "/home/interceptor/Документы/DATA/test5/fish4_1min.mp4"


cap = cv2.VideoCapture(path_video_src)

# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the total numer of frames in the video.
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

frame_number = 0
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)  # optional
success, frame = cap.read()

while success and frame_number <= frame_count:
    # do stuff

    frame_number += fps
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    success, frame = cap.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()