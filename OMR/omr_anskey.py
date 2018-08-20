import cv2
from cv2 import *
import numpy as np
import omr_helper as h
import pickle
import math


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
size =(500,700)
path ="2_001.jpg"
im= cv2.imread(path,1)
im= cv2.resize(im,size)
coord=h.coordinate(im)

# print coord

dst =im
x1= coord[3,0]
x2=coord[2,0]
y1=coord[3,1]
y2=coord[0,1]+2*coord[0,2]
dst= dst[y1:y2,x1:x2]
dst =cv2.resize(dst,size)
# cv2.imshow("circles",dst)
# cv2.waitKey()
# print dst.shape
xl=0
xr=500
xdiff= xr-xl
grid=xdiff/4
coord_c=[]
x1=0
y1=0
x2=500
y2=700
b= dst#[y1:y2,x1:x2]
img= dst[y1:y2,x1:x2]
b =cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
b=medianBlur(b,5)
# cv2.imshow("circles",b)
# cv2.waitKey()
ret,b = cv2.threshold(b,110,255, cv2.THRESH_BINARY)
# cv2.imshow("circles",b)
# cv2.waitKey()
contours, hier = cv2.findContours(b, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
disp = []
for i in range(0,4):
	x1= xl+(i*grid)
	x2= xl+((i+1)*grid)
	coord1=[]
	for cnt in contours:
		(x,y),radius = cv2.minEnclosingCircle(cnt)
		if (x1<x<x2):
			if(3<radius<7):
				if(int(y)>140):
					center = (int(x),int(y))
					radius = int(radius)
					disp.append(distn(int(x),int(y),coord))
					# coord1.append((center[0],center[1]))
					dist=math.hypot(center[0]-coord[3,0],center[1]-coord[3,1])
					coord1.append([center[1]-coord[3,1],dist,center[0]-coord[3,0]])
					cv2.circle(img,center,radius,(0,255,0),2)
				
	cv2.imshow("circles",img)
	cv2.waitKey(1000)
	d=np.array(coord1)
	ziped_list=zip(*d)
	x_list= list(ziped_list[0])		
	dic=dict(zip(x_list,d))
	x_list.sort()
	for i in x_list:
		coord_c.append(dic[i])

coord_c =np.array(coord_c)

# print coord_c

print "TOTAL ANS FOUND IN ANSWER KEY  = " + str(len(disp))
with open("responses.txt",'wb') as f:
	pickle.dump(coord_c,f)
with open("distance.txt",'wb') as f:
	pickle.dump(disp,f)
