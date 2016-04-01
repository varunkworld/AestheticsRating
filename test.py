from __future__ import division
from PIL import Image
from numpy import *
import sys

filename = sys.argv[1]
im = array (Image.open(filename).convert('HSV'))
f = []

# exposure of light and colourfulness

f1 = 0

X,Y,T = im.shape

for i in range(0,X) :
	for j in range(0,Y) :
		h,s,v = im[i,j]
		f1 = f1 + v
f1 = f1 / (X*Y)


# saturation

f2 = 0

X,Y,T = im.shape

for i in range(0,X) :
	for j in range(0,Y) :
		h,s,v = im[i,j]
		f2 = f2 + s
f2 = f2 / (X*Y)


# hue

f3 = 0

X,Y,T = im.shape

for i in range(0,X) :
	for j in range(0,Y) :
		h,s,v = im[i,j]
		f3 = f3 + h
f3 = f3 / (X*Y)


# rule of thirds

f4 = 0

X,Y,T = im.shape

for i in range(int(X/3),int(2*X/3)) :
	for j in range(int(Y/3),int(2*Y/3)) :
		h,s,v = im[i,j]
		f4 = f4 + h
f4 = (f4*9) / (X*Y)

f5 = 0

X,Y,T = im.shape

for i in range(int(X/3),int(2*X/3)) :
	for j in range(int(Y/3),int(2*Y/3)) :
		h,s,v = im[i,j]
		f5 = f5 + s
f5 = (f5*9) / (X*Y)

f6 = 0

X,Y,T = im.shape

for i in range(int(X/3),int(2*X/3)) :
	for j in range(int(Y/3),int(2*Y/3)) :
		h,s,v = im[i,j]
		f6 = f6 + v
f6 = (f6*9) / (X*Y)

# size and aspect ratio

f7 = X+Y
f8 = X/Y

f.append(f1);
f.append(f2);
f.append(f3);
f.append(f4);
f.append(f5);
f.append(f6);
f.append(f7);
f.append(f8);

for i in range(0,len(f)) :
	print "f" + str(i+1) + " -> " + str(f[i])
