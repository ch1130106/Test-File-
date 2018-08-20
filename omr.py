import cv2 
from cv2 import *
import numpy as np

def filetring2(im):
	p,q = im.shape[:2]
	im2 = np.ones((p,q),np.uint8)
	print im2.shape ,p,q
	for x in range(0,p-1):
		for y in range(0,q-1):
			if im[x,y,2]>150 :
				if  im[x,y,1]<100 :
					if  im[x,y,0]<100 :
						im2[x,y]= 255

					else:
						im2[x,y] = 0
	print 
	# im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

	return im2



def filetring(im):

	p,q = im.shape[:2]
	for x in range(0,p-1):
		for y in range(0,q-1):
			if im[x,y]<150:
				im[x,y] = 0
			else:
				im[x,y] = 255

	return im

a = cv2.imread('romr.jpg')
a=cv2.resize(a,(1685,2288))
b= filetring2(a)
"""Algorithim to be followed--
-> Take omr sheet with four points at the corners.
-> use these points to get the orientation of the sheet
-> Make the orientation of the sheet suitable
-> Now find the centers of the circles using HoughCircles
-> fing circle with pixel values value=0(black)
-> mach these centers with the mapped responses on x-axis with the same question on 
	yaix with the another question.
-> +1 for match ,-1 for worng match ,0 for no match
-> read name of the person using hand written ocr.
"""
circles = cv2.HoughCircles(b,cv.CV_HOUGH_GRADIENT,1,20,
                            param1=10,param2=10,minRadius=0,maxRadius=30)

circles = np.uint16(np.around(circles))
# print circles 
coord=[]
responses=[]

for i in circles[0,:]:
	if i[2]>14:
		print i[2]
		coord.append((i[1],i[0]))
		cv2.circle(a,(i[0],i[1]),i[2],(0,255,0),2)
		cv2.circle(a,(i[0],i[1]),2,(0,0,255),3)
	# [(2160, 56), (148, 72), (138, 1582), (2160, 1582)]
	# [(2158, 1642), (110, 52), (110, 1632)]


"use coord to solve the omr"
print coord
cv2.imshow('seeing is believing ',a)
cv2.waitKey()