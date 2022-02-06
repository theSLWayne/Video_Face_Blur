"""
Extract details from the input video

"""

import moviepy.editor as mp

def extractAudio(vid_path):
    """
    Extract audio clip from input video

    :param vid_path: Path to input video
    :return: Extracted audio
    """

    clip = mp.VideoFileClip(vid_path)
    return clip.audio

