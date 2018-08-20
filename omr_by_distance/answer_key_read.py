import cv2
from process_omr import processing
import math
import pickle

# from evaluation_by_ratio import processing
akey = cv2.imread('answer_key.jpg')
akey_d,coorda,a =  processing(akey)
with open('answer_key.txt','wb') as ans:
	pickle.dump(akey_d,ans)
with open('answer_coor.txt','wb') as ans:
	pickle.dump(coorda,ans)
with open('answer_corner.txt','wb') as ans:
	pickle.dump(a,ans)