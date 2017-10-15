import numpy as np
import cv2

img = cv2.imread('iitr.jpg', flags=cv2.IMREAD_COLOR) #by default set to grayscale
print img.shape #display the size of the image and the channels
cv2.imshow('image', img)

#converting BGR image to grayscale 
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert the image to grayscale

img_blue = img #copy the image in an array
img_blue[:, :, 1] = 0 #putting the 1th i.e. second channel i.e. Green channel = 0
img_blue[:, :, 2] = 0 #putting the 2th i.e. third channel i.e. red channel = 0

cv2.imshow("blue", img_blue)
cv2.imshow("greyScale",grayImage)

k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite("gray_iitr.jpg", grayImage)
	print "saved image"
	cv2.destroyAllWindobws()	