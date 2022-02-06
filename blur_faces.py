"""
Entrypoint for face blurring process
"""

import argparse
import glog as logger
import os

from tools import blurredFrames, extractAudio, extractMetaData
from moviepy.video.io import ImageSequenceClip

def initArgs():
    """
    Initialize arguments

    :return: parsed arguments
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--video_path', type=str,
                        help='Path to the video file',
                        required=True)
    parser.add_argument('-od', '--output_directory', type=str,
                        help='Path of the directory where processed video should be saved to')
    parser.add_argument('-s', '--show_frames', type=strToBool,
                        help='Whether to show frames as they are processed or not (y/n)',
                        default=False)

def strToBool(value):
    """
    Convert argument string to boolean

    :param value: Value parsed in argument
    :return: Boolean value
    """

    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Unsupported value encountered for --show_frames.')

def validateArgs():
    pass

def createVideo():
    pass

def getFileName():
    pass

def blurVideoFaces():
    pass

if __name__ == '__main__':

    args = initArgs()
