"""
Input video processing that includes:
    - Break down video into individual frames
    - Detect faces in each frame
    - Blur detected faces

"""

import cv2

def printProgressBar (iteration, total, prefix = 'Progress', suffix = 'Complete', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Terminal progress bar function
    Thanks to Greenstick & Diogo of Stackoverflow (https://stackoverflow.com/a/34325723/2817832) for the function. 

    @params:
    :param iteration : current iteration (Int)
    :param total     : total iterations (Int)
    :param prefix    : prefix string (Str)
    :param suffix    : suffix string (Str)
    :param decimals  : positive number of decimals in percent complete (Int)
    :param length    : character length of bar (Int)
    :param fill      : bar fill character (Str)
    :param printEnd  : end character (e.g. "\r", "\r\n") (Str)
    :return:
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def convertToRGB(img):
    """
    Convert BGR images into RGB images.

    :param img: BGR image
    :return: RGB image    
    """

    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


