import cv2
from cv2 import *
import numpy as np
import omr_helper as h
import pickle
import math

size =(500,700)
path ="2_001.jpg"

im= cv2.imread(path,1)
im= cv2.resize(im,size)
coord=h.coordinate(im)
# print coord
coord_c,disp,roll=h.processing(im,coord,size)
# print roll

# print len(coord_c)
# print len(disp)
with open("responses.txt",'wb') as f:
	pickle.dump(coord_c,f)
with open("distance.txt",'wb') as f:
	pickle.dump(disp,f)
