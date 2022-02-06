"""
Entrypoint for face blurring process
"""

import argparse
import glog as logger
import os
from pathlib import Path
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

from tools import blurredFrames, extractAudio, extractMetaData

DEFAULT_SAVE_DIR = './outputs/'

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

    return parser.parse_args()

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

def validateArgs(args):
    """
    Validate script arguments

    :param args: Arguments
    :return:
    """
    assert os.path.exists(args.video_path), f'The specified video file path "{args.video_path}" does not exist.'

    if args.output_directory and not os.path.isdir(args.output_directory):
        logger.warning(f'''The specified output directory path does not exist. 
            Video will be saved in the default location {DEFAULT_SAVE_DIR}.''')

def getFileName(video_path, save_path):
    """
    Get new video file path

    :param video_path: Path of the original video
    :param save_path: Path of the directory that blurred video should be saved to
    :return: File path for blurred video
    """

    save_path = save_path if save_path else DEFAULT_SAVE_DIR

    video_path = Path(video_path)

    if not os.path.exists(save_path):
        path = Path(save_path)
        path.mkdir(parents=True, exist_ok=True)

    new_file_name = f'{video_path.stem}_blurred{video_path.suffix}'

    return os.path.join(save_path, new_file_name)


if __name__ == '__main__':

    args = initArgs()

    validateArgs(args)

    total_frames, fps = extractMetaData(vid_path=args.video_path)
    logger.info(f'{total_frames} frames detected at {fps} fps.')

    logger.info("Applying the blurring effect... Press 'q' to stop the process")
    blurred_frames = blurredFrames(vid_path=args.video_path,
                                    frame_count=total_frames,
                                    show=args.show_frames)

    logger.info('Extracting audio...')
    audio = extractAudio(vid_path=args.video_path)

    logger.info('Creating video...')
    final_video = ImageSequenceClip(sequence=blurred_frames, fps=fps)
    final_video.audio = audio

    file_name = getFileName(video_path=args.video_path,
                            save_path=args.output_directory)

    final_video.write_videofile(file_name)

