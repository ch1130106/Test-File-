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
path ="1_001.jpg"
im= cv2.imread(path,1)
im= cv2.resize(im,size)
coord=h.coordinate(im)
# print coord

dst =cv2.imread(path,1)
dst =cv2.resize(dst,size)
x1= coord[3,0]
x2=coord[2,0]
y1=coord[3,1]
y2=coord[0,1]+2*coord[0,2]
dst= dst[y1:y2,x1:x2]
dst =cv2.resize(dst,size)
# cv2.imshow("circles",dst)
# cv2.waitKey()

with open("responses.txt",'rb') as f:
	ans_key=pickle.load(f)
with open("distance.txt",'rb') as f:
	ans_dis=pickle.load(f)
# print len(ans_key)	

xl=0
xr=500
xdiff= xr-xl
grid=xdiff/4

coord_c=[]

x1=0
y1=0
x2=500
y2=700
b= dst[y1:y2,x1:x2]
img= dst[y1:y2,x1:x2]
b =cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
b=medianBlur(b,5)
# cv2.imshow("circles",b)
# cv2.waitKey()
ret,b = cv2.threshold(b,110,255, cv2.THRESH_BINARY)
# cv2.imshow("circles",b)
# cv2.waitKey()

contours, hier = cv2.findContours(b, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
disp=[]
roll_c = []
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
				else:
					if int(x) < 125:
						center = (int(x),int(y))
						radius = int(radius)
						roll_c.append((int(x),int(y)))
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
roll_c = sorted(roll_c,key = lambda x: int(x[0]))
# roll_c = sorted(roll_c,key = lambda x: int(x[1]))
print roll_c



check=np.zeros(ans_key.shape[:1])
check =check.astype("uint8")
ques=np.zeros(ans_key.shape[:3])
#######Reading Rollnumber Also################# 
refrol = [1,2,3,4,5,6,7,8,9,0]
rollno=[]
for x in range(0,8):

	ser = float(roll_c[x][1]-19)/11
	if (abs(ser-int(ser)>0.49)):
		ser = int(ser)+1
	rollno.append(refrol[int(ser)])
	
	

print "Roll no = " ,rollno





###############################################

x=0

for i in range(0,200):
	v1=coord_c[i-x][0]
	v2=ans_key[i][0]
	y=v1-v2
	if (-4<y<4):
		ques[i][1]=coord_c[i-x][1]
		ques[i][0]=coord_c[i-x][0]
		ques[i][2]=coord_c[i-x][2]
	else:
		x=x+1

check=[]
for i in range(0,200):
	v1=ques[i][1] 
	v2= ans_key[i][1]
	y=v1-v2
	v1=ques[i][2] 
	v2= ans_key[i][2]
	x=v1-v2
	if (-2<y<2):
		if(-3<x<3):
			t=i+1
			check.append(t)


# print (check)
# print disp
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

