import argparse
import cv2
import dlib
import imutils
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
from scipy.spatial import distance as dist
import time

def eye_aspect_ratio(eye):
    # compute the euclidean distance between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    return ear

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True, help="path to facial landmark predictor")
ap.add_argument("-v", "--video", type=str, default="", help="path to input video file")
args = vars(ap.parse_args())

# define two constants, one for the eye aspect ratio to
# indicate blink and then a second constant for the
# number of consecutive frames the eye must be below the
# threshold
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3

# intialize the frame counters and the total number of blinks
COUNTER = 0
TOTAL = 0

# intialize dlib's face detector (HOG-based) and then create the facial
# landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args['shape_predictor'])

# grab the indexes of the facial landmarks for the left and right eye
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

print("[INFO] starting video stream thread...")
""" If you’re using a file video stream """
# vs = FileVideoStream(args['video']).start()
# fileStream = True
""" If you want to use a built-in webcam or USB camera """
vs = VideoStream(src=0).start()
""" For a Raspberry Pi camera module """
# vs = VideoStream(usePiCamera=True).start()
fileStream = False
time.sleep(1.0)

# loop over frames from the video stream
while True:
    # if this is a file video stream, then we need to check if there
    # any more frames left in the buffer to process
    if fileStream and not vs.more():
        break
    
    # grab the frame from the threaded video file stream, resize it, and 
    # convert it to grayscale channels
    frame = vs.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame
    rects = detector(gray, 0)

    # loop over the faces
    for rect in rects:
        # determine the facial landmarks for the face region, then 
        # convert the facial landmark (x, y)-coordinates to a Numpy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # extract the left and right eye coordinates, then use them to 
        # compute the ear for both eyes
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leaftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # average the EAR for both eyes
        ear = (leaftEAR + rightEAR) / 2.0
        
        # compute the convex hull for the left and right eye, then 
        # visualize each of the eyes
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # check if the eye aspect ratio is below the blink threshold, and 
        # if so, incement the blink frame counter
        if ear < EYE_AR_THRESH:
            COUNTER += 1
        else:
            # otherwise, the eye aspect ratio is not below the blink
            # threshold
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                # if the eyes were closed for a sufficient number of then
                # increment the total number of blinks
                TOTAL += 1
            # reset the eye frame counter
            COUNTER = 0
    
        # draw the total number of blinks on the frame along with the 
        # computed eye aspect ratio for the frame
        cv2.putText(frame, 'Blinks: {}'.format(TOTAL), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cv2.destroyallWindows()
vs.stop
