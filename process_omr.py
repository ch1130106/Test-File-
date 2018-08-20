import cv2
from cv2 import *
import numpy as np
import math



def processing(imm):
	def filetring(im):

		p,q = im.shape[:2]
		im2 = np.ones((p,q),np.uint8)
		for x in range(0,p-1):
			for y in range(0,q-1):
				if im[x,y,2]>150 :
					if  im[x,y,1]<100 :
						if  im[x,y,0]<100 :
							im2[x,y]= 255

						else:
							im2[x,y] = 0
	 
		# im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

		return im2

	def cornors(im,idm):
		b=[]
		ret,im = cv2.threshold(im,80,255, cv2.THRESH_BINARY)
		contours, hier = cv2.findContours(im, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		for cnt in contours:
			(x,y),radius = cv2.minEnclosingCircle(cnt)
			center = (int(x),int(y))
			radius = int(radius)
			cv2.circle(idm,center,radius,(0,255,0),2)	
			b.append((int(x),int(y)))
		# cv2.imshow('dsadf',idm)
		# cv2.waitKey()

		return b
	def distn(x1,y1,l):
		x2 = l[0][0]
		y2 = l[0][1]
		x3 = l[1][0]
		y3 = l[1][1]
		x4 = l[2][0]
		y4 = l[2][1]
		x5 = l[3][0]
		y5 = l[3][1]
		d1 = int(math.sqrt((x1-x2)**2+(y1-y2)**2))
		d2 = int(math.sqrt((x1-x3)**2+(y1-y3)**2))
		d3 = int(math.sqrt((x1-x4)**2+(y1-y4)**2))
		d4 = int(math.sqrt((x1-x5)**2+(y1-y5)**2))

		return d1,d2,d3,d4

	dst =imm
	dst =cv2.resize(dst,(500,700))
	cimg =dst
	core = dst
	image = filetring(cimg)
	# cv2.imshow('hjkl',image)
	# cv2.waitKey()
	corners = cornors(image,core)
	corners = sorted(corners,key = lambda x: int(x[0]))
	corners = sorted(corners,key = lambda x: int(x[1]))

	# print corners

	dst =cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
	# cv2.imshow("circles",dst)
	# cv2.waitKey() 

	b=medianBlur(dst,5)
	# cv2.imshow("circles",b)
	# cv2.waitKey()

	ret,b = cv2.threshold(b,110,255, cv2.THRESH_BINARY)
	# cv2.imshow("circles",b)
	# cv2.waitKey()
	response=[]
	coord =[]
	contours, hier = cv2.findContours(b, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		(x,y),radius = cv2.minEnclosingCircle(cnt)
		if y >150:
			if(3<radius<7):
				center = (int(x),int(y))
				coord.append(center)
				response.append(distn(int(x),int(y),corners))
				radius = int(radius)
				cv2.circle(cimg,center,radius,(0,255,0),2)	
	# cv2.imshow("circles",cimg)
	# cv2.waitKey()
	coord = sorted(coord,key = lambda x: int(x[0]))
	coord = sorted(coord,key = lambda x: int(x[1]))
	return response,coord,corners

