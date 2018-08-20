import cv2
from process_omr import processing
import math
import pickle
# from evaluation_by_ratio import processing

response = cv2.imread('RESULT.jpg')

response_d,coordr,r= processing(response)
with open('answer_key.txt','rb') as ans:
	akey_d =  pickle.load(ans)
with open('answer_coor.txt','rb') as ans:
	coorda = pickle.load(ans)
with open('answer_corner.txt','rb') as ans:
	a= pickle.load(ans)
# ratio1 = float(fponts[0][0] - fponts[1][0])/((corners[0][0] - corners[1][0]))
# ratio2 = float(fponts[2][0] - fponts[3][0])/((corners[2][0] - corners[3][0]))
# ratio3 = float(fponts[0][1] - fponts[2][1])/((corners[0][1] - corners[2][1]))
# ratio4 = float(fponts[1][1] - fponts[3][1])/((corners[1][1] - corners[3][1]))
# print ratio1,ratio2,ratio3,ratio4
print len(coorda)
print len(coordr)
print r
print a
# print coordr
# d1 = distn(fponts[0][0],fponts[0][1],fponts[1][0],fponts[1][1],1,1)
# d2 = distn(fponts[0][0],fponts[0][1],fponts[2][0],fponts[2][1],1,1)
# d3 = distn(corners[0][0],corners[0][1],corners[1][0],corners[1][1],1,1)
# d4 = distn(corners[0][0],corners[0][1],corners[2][0],corners[2][1],1,1)
# ratio1 = d1/d3
# ratio2 = d2/d4
# print distn(coordr[0][0],http://www.math.chalmers.se/~rudemo/statimage.htmlcoordr[0][1],fponts[0][0],fponts[0][1],ratio1,ratio2) ,akey_d[0]

pmarks = 0
nmarks = 0
match=[]
wrong=[]
for y in range(0,len(response_d)):
	for x in range(0,len(akey_d)):
		if abs(response_d[y][0]-akey_d[x][0])<5:
			if abs(response_d[y][1]-akey_d[x][1])<5:
				if abs(response_d[y][2]-akey_d[x][2])<5:
					if abs(response_d[y][3]-akey_d[x][3])<5:
						pmarks=pmarks+4
						match.append(response_d[y])
						wrong.append(akey_d[x])

nmarks = (len(response_d)-len(match))*-1
print match
print wrong

print pmarks,nmarks
# print wrong
