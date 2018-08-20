import cv2
from cv2 import *
import numpy as np
import omr_helper as h
import pickle
import math

size =(500,700)
path ="1_001.jpg"

im= cv2.imread(path,1)
im= cv2.resize(im,size)
coord=h.coordinate(im)
# print coord
coord_c,disp,rollno=h.processing(im,coord,size)
print "ROLLNO IS "+str(rollno)

with open("responses.txt",'rb') as f:
	ans_key_c=pickle.load(f)
with open("distance.txt",'rb') as f:
	ans_dis=pickle.load(f)

for j in range(0,4):
	ans_key=ans_key_c[:,j]
	coord=coord_c[:,j]
	# print ans_key.shape,coord.shape
	ques=np.zeros(ans_key.shape[:2])
	x=0
	for i in range(0,200):
		v1=coord[i-x][1]
		v2=ans_key[i][1]
		# print v2
		y=v1-v2
		# print y
		if (-4<y<4):
			ques[i][0]=coord[i-x][0]
			ques[i][1]=coord[i-x][1]
			ques[i][2]=coord[i-x][2]
			ques[i][3]=coord[i-x][3]
			ques[i][4]=coord[i-x][4]

		else:
			x=x+1

	check=[]
	centre=[]
	for i in range(0,200):
		v1=ques[i][2] 
		v2= ans_key[i][2]
		y=v1-v2
		v1=ques[i][0] 
		v2= ans_key[i][0]
		x=v1-v2
		if (-2<y<2):
			if(-3<x<3):
				t=i+1
				check.append(t)
				centre.append((ques[i,3],ques[i,4]))
	# print check
	# print len(check)
	# print centre

# print type(disp)
final_check=[]
for y in range (0,len(disp)):
	for x in range(0,len(ans_dis)):
		if abs(disp[y][0]-ans_dis[x][0])<6:
			if abs(disp[y][1]-ans_dis[x][1])<6:
				if abs(disp[y][2]-ans_dis[x][2])<6:
					if abs(disp[y][3]-ans_dis[x][3])<6:
						final_check.append(disp[y])
print "TOTAL QUESTIONS ATTEMPTED = "+str(len(disp))
print "Correct answers =" + str(len(final_check))
print "Incorrect answers are = " + str(abs(len(final_check)-len(disp)))

