#image processing 
import cv2
# mathematical work
import numpy as np

import PIL.Image

import sys

from face_recognition import *

import os

from datetime import datetime
#face_cascade=cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
#capture videos from the camera
print("Do you want to take test image [y,n ]-->")
option=input()
#print("Enter Your Id-->")
#id=int(sys.stdin.readline())

if(option == 'y'  ) :
	
	cap=cv2.VideoCapture(0)
	sampleNum=0
	while 1:
		ret,img=cap.read()
		#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		#faces=face_cascade.detectMultiScale(gray,1.3,5)
		#faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
        

		sampleNum +=1
		#roi_gray = gray[y:y+h, x:x+w]
		t=datetime.now().time()
		d=datetime.now().date()
		faceFileName="test_data/"+str(d)+"__"+str(t)+".jpg"
		face_location = face_locations(np.array(img))
		if(len(face_location)<1):
			print("no face found \n")
			continue
		cv2.imwrite(faceFileName,img)
    




	
		#cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		cv2.waitKey(1000)
		cv2.imshow('face',img)
		cv2.waitKey(100)
		if(sampleNum>0):
			break
	cap.release()






cv2.destroyAllWindows()
	
	
