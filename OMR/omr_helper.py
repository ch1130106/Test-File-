import cv2
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
  coord =np.array(coord)
  coord_arrange=[]
  if(coord[0,0]<coord[1,0]):
    coord_arrange.append(coord[1])
    coord_arrange.append(coord[0])
  else:
    coord_arrange.append(coord[0])
    coord_arrange.append(coord[1])  
  if(coord[2,0]<coord[3,0]):
    coord_arrange.append(coord[3])
    coord_arrange.append(coord[2])
  else:
    coord_arrange.append(coord[2])
    coord_arrange.append(coord[3])  
  coord_arrange =np.array(coord_arrange)  
  return coord_arrange 

def angle(coord):
  p4,p3,p2,p1 =(coord[0],coord[1],coord[2],coord[3])

  if(p3[0]<p4[0]):
    p1x,p1y=p3[0],p3[1]
  else:
    p1x,p1y=p4[0],p4[1] 
    
  if(p1[0]>p2[0]):
    p2x,p2y=p1[0],p1[1]
  else:
    p2x,p2y=p2[0],p2[1]

  if p1y>p2y:
    v1= p1y-p2y
  else:
    v1= p2y-p1y
      
  if p1x>p2x:
    v2= p1x-p2x
  else:
    v2= p2x-p1x
    
  val=float(v1)/v2 
  # print val
  th2 = math.degrees(math.atan(val))  
  return th2

