"""
Input video processing that includes:
    - Break down video into individual frames
    - Detect faces in each frame
    - Blur detected faces

"""

import cv2

def printProgressBar(iteration, total, prefix = 'Progress', suffix = 'Complete', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Terminal progress bar function
    Thanks to Greenstick & Diogo of Stackoverflow (https://stackoverflow.com/a/34325723/2817832) for the function. 

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

def blurredFrames(vid_path, frame_count, show=False):

    """
    Return chronological list of frames with blurred faces

    :param vid_path: Path to the video
    :param frame_count: Total number of frames in the input video file
    :param show: Whether the frames should be shown as they are processed
    :return: List of frames with blurred faces in chronological order
    """

    # Frame counter
    frames = 0

    # Blurred Frames list
    blurred_frames = []

    # Load video
    vid = cv2.VideoCapture(vid_path)

    # Loop till the end of the video
    while(vid.isOpened()):
        ret, frame = vid.read()

        # Convert frame to grayscale to make it easier for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Haar Cascade model to detect faces
        haar_face_casscade = cv2.CascadeClassifier('cascade_files/haarcascade_frontalface_alt.xml')

        # Detect faces
        faces = haar_face_casscade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=4)

        # Loop through all faces detected
        for (x, y, w, h) in faces:

            # Apply blur to detected face
            roi = frame[y:y+h, x:x+w]
            roi = cv2.GaussianBlur(roi, (43, 43), 30)
            frame[y:y+roi.shape[0], x:x+roi.shape[1]] = roi

        # Append blurred frames to the list
        blurred_frames.append(convertToRGB(frame))

        # Display current frame - after blurring
        if show:
            cv2.imshow('Frame', frame)

        # Update progressbar
        frames += 1
        printProgressBar(frames, frame_count)

        # Break loop if all frames are iterated through
        if frames == frame_count:
            break

        # Define "q" as the exit button to stop the process
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the loaded video object
    vid.release()

    # Close all windows opened to display frames
    cv2.destroyAllWindows()

    return blurred_frames


