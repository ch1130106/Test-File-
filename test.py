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


b = [(2160, 56), (148, 72), (138, 1582), (2160, 1582)]
b = validity(b,2155,65,140,1580)
print b