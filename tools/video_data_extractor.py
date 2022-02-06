"""
Extract details from the input video

"""

import moviepy.editor as mp
import cv2

def extractAudio(vid_path):
    """
    Extract audio clip from input video

    :param vid_path: Path to input video
    :return: Extracted audio
    """

    # Read video file
    clip = mp.VideoFileClip(vid_path)
    return clip.audio # Extracted audio

def extractMetaData(vid_path):
    """
    Extract total frame count and fps from input video

    :param vid_path: Path to input video
    :return: (number of total frames, fps)
    """

    # Read video frame-by-frame
    clip = cv2.VideoCapture(vid_path)

    # Get frame count of the video
    total = int(clip.get(cv2.CAP_PROP_FRAME_COUNT))
    # FPS of the video
    fps = int(clip.get(cv2.CAP_PROP_FPS))

    return total, fps

