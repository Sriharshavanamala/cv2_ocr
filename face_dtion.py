import cv2
import os

#create cascade classifier object

face_cascade=cv2.CascadeClassifier("C:\\Users\Armed Bunker\\Pictures\haarcascade_frontalface_alt.xml")

#Read Image as it is

img=cv2.imread("F:\\New folder (2)\\IMG-20191124-WA0040.jpg")
#cv2.imshow('show',img)
image_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('show2',image_grey)
faces = face_cascade.detectMultiScale(image_grey, scaleFactor = 1.05,minNeighbors = 5)
print(type(faces))

for (x, y, w, h) in faces:
   #print(y)
    img_c=cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)										
    cv2.imshow('show',img)
    cv2.waitKey(0)
	
