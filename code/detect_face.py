import numpy as np
import cv2

#initialise the XML files provided by OpenCV and use them to detect the presence of 
# a face in an image and eyes in that corresponding part of the image
face_cascade = cv2.CascadeCladedssifier('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_eye.xml')

#read the image
img = cv2.imread('kohli.jpg')

#resiing the image to 480, 360
img = cv2.resize(img, (480, 360))
#creating a grayscale copy of the image for detecting an eye
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#finding out the faces in the image by convoluting 
# with boxes of size reducing by 1.3
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#after having found the boxes drawing the bounding boxes
for (x,y,w,h) in faces:
	#drawing a rectangle around the faces found in the image
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    #detecting eyes inside the bounding box of the face
    for (ex,ey,ew,eh) in eyes:
    	# drawing rectangles around the eyes in a bounding box of face
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#display the images
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
