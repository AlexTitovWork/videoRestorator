#!/usr/bin/env python3

from restorator.video_restorator import *

if __name__ == '__main__':
    # path_video_src = "resources/video_input.mp4"
    # path_video_dst = "resources/video_output.mp4"

    # path_video_src = "../../Git_repo_telesoft/DATA/test6_leave/master2_qa.mp4"
    path_video_src = "./resources/fish8_leave.mp4"

    path_video_dst = "./resources/fish8_qa_restored.mp4"

    restrore_and_transcode(path_video_src, path_video_dst)
    #debug()
