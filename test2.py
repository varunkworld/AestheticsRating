from __future__ import division
import pywt
import numpy as np
from PIL import Image


im = np.array(Image.open('empire.jpg').convert('HSV'))
X,Y,T = im.shape
print X,Y
h = []
s = []
v = []

for i in range(0,X) :
	p = []
	q = []
	r = []
	for j in range(0,Y) :
		a,b,c = im[i][j]
		p.append(a)
		q.append(b)
		r.append(c)
	h.append(p)
	s.append(q)
	v.append(r)
h = np.array(h)
s = np.array(s)
v = np.array(v)


# wavelet transform on hue
'''
'''
coeffs = pywt.wavedec2(h, 'db1', level=3)
cA3, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs


#print str(cH3.shape) + str(cH2.shape) + str(cH1.shape)
c1 = min(cH1.shape[0],cH1.shape[1])
c2 = min(cH2.shape[0],cH2.shape[1])
c3 = min(cH1.shape[0],cH1.shape[1])

print (np.linalg.det(np.array(cH1[0:c1][0:c1])))
# level1
f10 = (np.sum(cH1) + np.sum(cV1) + np.sum(cD1))#/(np.nlinalg.det(cH1)+np.nlinalg.det(cV1)+np.nlinalg.det(cD1))

# level2
f11 = (np.sum(cH2) + np.sum(cV2) + np.sum(cD2))#/(np.linalg.det(cH2)+np.linalg.det(cV2)+np.linalg.det(cD2))

# level3
f12 = (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))#/(np.linalg.det(cH3)+np.linalg.det(cV3)+np.linalg.det(cD3))

print f10,f11,f12


# wavelet transform on saturation

coeffs = pywt.wavedec2(s, 'db1', level=3)
cA3, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs

# level1
f13 = (np.sum(cH1) + np.sum(cV1) + np.sum(cD1))#/(np.nlinalg.det(cH1)+np.nlinalg.det(cV1)+np.nlinalg.det(cD1))

# level2
f14 = (np.sum(cH2) + np.sum(cV2) + np.sum(cD2))#/(np.linalg.det(cH2)+np.linalg.det(cV2)+np.linalg.det(cD2))

# level3
f15 = (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))#/(np.linalg.det(cH3)+np.linalg.det(cV3)+np.linalg.det(cD3))

print f13,f14,f15

# wavelet transform on value

coeffs = pywt.wavedec2(v, 'db1', level=3)
cA3, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs

# level1
f16 = (np.sum(cH1) + np.sum(cV1) + np.sum(cD1))#/(np.nlinalg.det(cH1[0:cH1.shape[0]][0:])+np.nlinalg.det(cV1)+np.nlinalg.det(cD1))

# level2
f17 = (np.sum(cH2) + np.sum(cV2) + np.sum(cD2))#/(np.linalg.det(cH2)+np.linalg.det(cV2)+np.linalg.det(cD2))

# level3
f18 = (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))#/(np.linalg.det(cH3)+np.linalg.det(cV3)+np.linalg.det(cD3))

print f16,f17,f18

x = int(X/4)
y = int(Y/4)
print x,y
count = 0
countx = 0
mh = []
ms = []
mv = []
while count < 16 :
	p1 = []
	p2 = []
	p3 = []
	for i in range(x*countx,x*countx+x) :
		temp1 = []
		temp2 = []
		temp3 = []
		#print str(x*countx)+","+str(x*countx+x)+ " " +str(y*(count%4))+","+str(y*(count%4)+y)
		for j in range(y*(count%4),y*(count%4)+y) :
			#print str(countx)+","+str(count) + "->" + str(i)+","+str(j)
			temp1.append(h[i][j])
			temp2.append(s[i][j])
			temp3.append(v[i][j])
		p1.append(temp1)
		p2.append(temp2)
		p3.append(temp3)
	mh.append(p1)
	ms.append(p2)
	mv.append(p3)
	count = count + 1
	if count % 4 == 0 :
		countx = countx + 1



# hue
numerator = 0
denominator = 0
for i in range(0,16) :
	coeffs = pywt.wavedec2(mh[i], 'db1', level=3)
	cA3, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs
	if i == 6 or i == 7 or i == 10 or i == 11 :
		numerator = numerator + (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))
	denominator = denominator + (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))
f53 = numerator/denominator
print f53
# saturation
numerator = 0
denominator = 0
for i in range(0,16) :
	coeffs = pywt.wavedec2(ms[i], 'db1', level=3)
	cA3, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs
	if i == 6 or i == 7 or i == 10 or i == 11 : 
		numerator = numerator + (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))
	denominator = denominator + (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))
f54 = numerator/denominator
print f54
# value
numerator = 0
denominator = 0
for i in range(0,16) :
	coeffs = pywt.wavedec2(mv[i], 'db1', level=3)
	cA3, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs
	if i == 6 or i == 7 or i == 10 or i == 11 :
		numerator = numerator + (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))
	denominator = denominator + (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))
f55 = numerator/denominator
print f55