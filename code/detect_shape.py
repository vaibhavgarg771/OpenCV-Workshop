# This code tries to detect a particular color in a video 
# and draw it's trail
#I have done this for the color Blue

from collections import deque
import numpy as np
import argparse

#if this line gives an error just open CMD/ Terminal and run 
# pip install imutils
import imutils
import cv2
 
#creating a queue of default size 64 to store the previous positions 
#of our color of interest and then joining those points

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args())
# define the lower and upper boundaries of the "blue"
# ball in the HSV color space, then initialize the
# list of tracked points
blueLower = (110, 50, 50)
blueUpper = (130, 255, 255)
pts = deque(maxlen=args["buffer"])
 
camera = cv2.VideoCapture(0)

while True:
    # grab the current frame
    (grabbed, frame) = camera.read()
 
    # resize the frame and convert it to the HSV
    # color space

    frame = imutils.resize(frame, width=600)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    # construct a mask for the color "blue", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, blueLower, blueUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
 
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
 
    # update the points queue
    pts.appendleft(center)
    # loop over the set of tracked points
    for i in xrange(1, len(pts)):
        # if either of the tracked points are None, ignore
        # them
        if pts[i - 1] is None or pts[i] is None:
            continue
 
        # otherwise, compute the thickness of the line and
        # draw the connecting lines
        # thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), 2)
    
    #flipping the frame so that you can see an image as you would in a mirror
    flip = cv2.flip(frame, 1)
    # show the frame to our screen
    cv2.imshow("Frame", flip)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()