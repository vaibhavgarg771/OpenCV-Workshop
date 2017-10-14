import numpy as np
import cv2

img = cv2.imread('caps.jpg', flags=cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# sensitivity = 25
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

# Threshold the HSV image to get only blue colors
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Bitwise-AND mask and original image
res_blue = cv2.bitwise_and(img, img, mask= mask_blue)
res_green = cv2.bitwise_and(img, img, mask=mask_green)

cv2.imshow('image',img)
cv2.imshow('mask_blue',mask_blue)
cv2.imshow('mask_green',mask_green)
cv2.imshow('res_blue',res_blue)
cv2.imshow('res_green',res_green)

cv2.waitKey(0)
cv2.destroyAllWindows()