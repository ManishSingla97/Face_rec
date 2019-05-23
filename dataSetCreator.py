
# This file is for taking the student entry.
# Student will be asked for name, regNo and id


import cv2

import numpy as np

import PIL.Image


import sys

from face_recognition import *

import os

from database_entry import checkDatabase

#get the name from the terminal
print("Enter Your Name-->")
name=str(sys.stdin.readline())

#get the id
print("Enter Your regNo-->")
Id=int(sys.stdin.readline())

#get the roll
print("Enter Your roll-->")
roll=int(sys.stdin.readline())

Name = name
Name1 = Name.split("\n")

#make entry of student in the  database if not  already present
checkDatabase(Id, Name1[0], roll) 


#create an object of VideoCapture
cap=cv2.VideoCapture(0)                       #0 corresponods to system's camera
sampleNum=0
#folder's name
folderName="training_data/"+name+str(Id)

#make folder if not exist in the database
if not os.path.exists(folderName):
	os.makedirs(folderName)
while 1: 
        #img contains the image frame and ret contains true or false
	ret,img=cap.read()
	sampleNum +=1
	#image full path with image name


	faceFileName="training_data/"+name+str(Id)+"/"+str(sampleNum)+".jpg"
	face_location = face_locations(np.array(img))
	if(len(face_location)<1):
		print("no face found")
		continue
	elif(len(face_location)>1):
		print("more than one face")
		continue
	


	#save the image
  
	cv2.imwrite(faceFileName,img)
	#show the image to the user

	cv2.imshow('face',img)
	cv2.waitKey(1000)
	if(sampleNum>4):
		break
#release the cap
cap.release()
#destroy all open windows
cv2.destroyAllWindows()
	
	
