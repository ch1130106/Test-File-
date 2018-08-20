import cv2
from cv2 import *
import numpy as np
import math

def coordinate(a):
  B,G,R = cv2.split(a)
  test = R
  r,c= test.shape[:2]
  img =np.zeros((r,c))

  for i in range(0,r):
    for j in range(0,c):
      vr =R[i][j]
      vg =G[i][j]
      vb =B[i][j]
      if vr>200 and vg<120 and vb<120:
        img[i][j]=vr

  img =img.astype("uint8")
  # cv2.imshow("dsad",img)
  # cv2.waitKey()
  cimg =a
  coord =[]
  contours, hier = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  x1,y1=0,0
  for cnt in contours:
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    dist=math.hypot(x-x1,y-y1)
    if(4<radius<8):
      if(dist>c/2):
        center = (int(x),int(y))
        radius = int(radius)
        x1,y1=center[0],center[1]
        coord.append((center[0],center[1],radius))
        cv2.circle(cimg,center,radius,(0,255,0),2)  
  # cv2.imshow("dsad",cimg)
  # cv2.waitKey()
  
  coord= sorted(coord,key = lambda x: int(x[0]))
  coord=sorted(coord,key = lambda x: int(x[1]))
  coord =np.array(coord)
  # print coord  
  return coord

def angle(coord):
  p1,p2,p3,p4 =(coord[0],coord[1],coord[2],coord[3])
  p1x,p1y=p3[0],p3[1]
  p2x,p2y=p1[0],p1[1]
  v1= p1y-p2y
  v2= p2x-p1x
  val=float(v1)/v2 
  # print val
  th2 = math.degrees(math.atan(val))  
  return th2

def distn(x1,y1,l):
  x2 = l[0][0]
  y2 = l[0][1]
  x3 = l[1][0]
  y3 = l[1][1]
  x4 = l[2][0]
  y4 = l[2][1]
  x5 = l[3][0]
  y5 = l[3][1]

  x1diff,y1diff = (x1-x2),(y1-y2)
  x2diff,y2diff = (x1-x3),(y1-y3)
  x3diff,y3diff = (x1-x4),(y1-y4)
  x4diff,y4diff = (x1-x5),(y1-y5)
  d1= math.hypot(x1diff,y1diff)
  d2= math.hypot(x2diff,y2diff)
  d3= math.hypot(x3diff,y3diff)
  d4= math.hypot(x4diff,y4diff)

  return (d1,d2,d3,d4),((x1diff,y1diff,d1,x1,y1),(x2diff,y2diff,d2,x1,y1),(x3diff,y3diff,d3,x1,y1),(x4diff,y4diff,d4,x1,y1))

def processing(dst,coord,size):
  x1= coord[0,0]
  x2=coord[1,0]
  y1=coord[0,1]
  y2=coord[3,1]+2*coord[3,2]
  dst= dst[y1:y2,x1:x2]
  dst =cv2.resize(dst,size)
  cimg =dst
  # cv2.imshow("circles",dst)
  # cv2.waitKey()
  roll_c=[]
  xl=0
  xr=500
  xdiff= xr-xl
  grid=xdiff/4

  coord_c=[]

  b=dst
  img=dst
  b =cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
  b=medianBlur(b,5)
  cv2.imshow("circles",b)
  cv2.waitKey()
  ret,b = cv2.threshold(b,110,255, cv2.THRESH_BINARY)
  cv2.imshow("circles",b)
  cv2.waitKey()
  contours, hier = cv2.findContours(b, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  disp=[]
  for i in range(0,4):
    x1= xl+(i*grid)
    x2= xl+((i+1)*grid)
    coord1=[]
    dist_arrange=[]
    for cnt in contours:
      (x,y),radius = cv2.minEnclosingCircle(cnt)
      if (x1<x<x2):
        if(3<radius<7):
          if(int(y)>140):
            center = (int(x),int(y))
            radius = int(radius)
            dist =distn(int(x),int(y),coord)
            disp.append(dist[0])
            coord1.append(dist[1])
            #(d1,d2,d3,d4),((x1diff,y1diff,d1,x1,y1),(x2diff,y2diff,d2,x1,y1),(x3diff,y3diff,d3,x1,y1),(x4diff,y4diff,d4,x1,y1))
            cv2.circle(img,center,radius,(0,255,0),2)
          else:
            if int(x) < 125:
              center = (int(x),int(y))
              radius = int(radius)
              roll_c.append((int(x),int(y)))
              cv2.circle(img,center,radius,(0,255,0),2)

    cv2.imshow("circles",img)
    cv2.waitKey()
    dist_list=[]
    for x in range(0,4): 
      dt=zip(*coord1)
      # print dt
      d=dt[x]
      d= sorted(d,key=lambda l:int(l[1]))
      dist_list.append(d)
    dist_list =zip(*dist_list)  
    coord_c=coord_c+dist_list
  roll_c = sorted(roll_c,key = lambda x: int(x[0]))
  # print roll_c
  coord_c =np.array(coord_c) 
  #######Reading Rollnumber Also################# 
  refrol = [1,2,3,4,5,6,7,8,9,0]
  rollno=[]
  for x in range(0,8):

    ser = float(roll_c[x][1]-19)/11
    if (abs(ser-int(ser)>0.49)):
      ser = int(ser)+1
    rollno.append(refrol[int(ser)])






###############################################
  # print coord_c.shape
  # print coord_c[0]
  return coord_c,disp,rollno