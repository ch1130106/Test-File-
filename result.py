import cv2 
from cv2 import *
import numpy as np

def filetring(im):
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



def validity(l,x1,y1,x2,y2):
	x = len(l)
	b=[]
	for y in l:
		if (y[0]<(x1+10) and y[0]> x1-10):
			if (y[1]<(y1+10) and y[1]> y1-10):
				b.append(y)
			else:
				if (y[1]<(y2+10) and y[1]> y2-10):
					b.append(y)
		else:
			if  (y[0]<(x2+10) and y[0]> x2-10):
				if (y[1]<(y1+10) and y[1]> y1-10):
					b.append(y)
				else:
					if (y[1]<(y2+10) and y[1]> y2-10):
						b.append(y)
	return b




a = cv2.imread('RESULT.jpg')

b = filetring(a)


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
	#20,30  18,471  469,31 469,472

print coord
coord = validity(coord,2155,65,140,1580)
print coord
cv2.imshow('seeing is believing ',a)
cv2.waitKey()