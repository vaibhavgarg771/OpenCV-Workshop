# this code tries to run color detection on a video 

import numpy as np
import cv2

#initialise your camera
cap = cv2.VideoCapture(0)

# run an infinite loop for your video, 
# instead of this you could read any video 
# on your system and process that
while (1):
	# capturing the individual frames of the video
	_, frame = cap.read()
	# converting each frame from RGB to HSV values
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# HSV range for blue color
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)

	# display the original video, the mask and the resultant video
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	# break the infinite loop if 'esc' key is pressed	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()
