from __future__ import division
from PIL import Image
import numpy as np
from scipy import misc
import pywt
import numbers
import math
import cv2

#filename = sys.argv[1]
#filename='abc.jpg'

#direct= path to the dataset directory
direct='K:\Old\E_DRIVE\ACADEMICS IV\BTP\April\FE\Pydownloaded'


def getFeatureVector(filename) :

        f=[]
      # open the image
        img = Image.open(direct+"\\"+filename)    #file = open(direct+"\\"+str, "r")
        #img=Image.open(str)

        # grab width and height
        width, height = img.size

        # make a list of all pixels in the image
        pixels = img.load()
        if isinstance(pixels[0,0] ,numbers.Integral) :
                        #print(" INVALID FILE: "+str,end=" ")
                        img.close()
                        return(-2,-2,-2)  #indicating file is not in required pixel format
        else :
                data = []
                for x in range(width):
                    for y in range(height):
                        aPixel = pixels[x, y]
                        data.append(aPixel)

                r = 0
                g = 0
                b = 0
                counter = 0

                # loop through all pixels
                # if alpha value is greater than 200/255, add it to the average
                # (note: could also use criteria like, if not a black pixel or not a white pixel...)
                for x in range(len(data)):
                    try:
                        #if (data[x][3]) > 200 :
                            r+=data[x][0]
                            g+=data[x][1]
                            b+=data[x][2]
                    except:
                        r+=(data[x][0])
                        g+=data[x][1]
                        b+=data[x][2]

                    counter+=1
                    #End for
                rgbAvg=[]    
                # compute average RGB values
                rAvg = r/counter;rgbAvg.append(rAvg)
                gAvg = g/counter;rgbAvg.append(gAvg)
                bAvg = b/counter;rgbAvg.append(bAvg)

                #you can also return rounded values upto required precision using round
                #return (rAvg, gAvg, bAvg)
                
        img=img.convert('RGB')
               
        counter = 0
        brightness=0
        LuminanceA=0
        LuminanceB=0
        LuminanceC=0
        
        # loop through all pixels,calculates each property for every pixel
        # if alpha value is greater than 200/255, add it to the average
        # (note: could also use criteria like, if not a black pixel or not a white pixel...)
        for x in range(len(data)):
                    try:
                        #if (data[x][3]) > 200 :
        
                            brightness+=(data[x][0]+data[x][1]+data[x][2])/3
                            #Standard
                            LuminanceA+=( 0.2126*data[x][0] + 0.7152*data[x][1]+0.0722*data[x][2])
                            #Percieved A
                            LuminanceB+=(0.299*data[x][0]+0.587*data[x][1]+0.114*data[x][2])
                            #Perceived B, slower to calculate
                            LuminanceC+=math.sqrt(0.241*(data[x][0])*(data[x][0])+0.691*(data[x][1])*(data[x][1])+0.068*(data[x][2])*(data[x][2]))
                    except:
                            brightness+=(data[x][0]+data[x][1]+data[x][2])/3
                            LuminanceA+=( 0.2126*data[x][0] + 0.7152*data[x][1]+0.0722*data[x][2])
                            LuminanceB+=(0.299*data[x][0]+0.587*data[x][1]+0.114*data[x][2])
                            LuminanceC+=math.sqrt(0.241*(data[x][0])*(data[x][0])+0.691*(data[x][1])*(data[x][1])+0.068*(data[x][2])*(data[x][2]))


                    counter+=1
                    #End for        
        # compute average values
        brightnessAvg = brightness/counter; 
        LA_Avg = LuminanceA/counter;
        LB_Avg = LuminanceB/counter;
        LC_Avg = LuminanceC/counter;
        #you can also return rounded values upto required precision using round
        f.append(brightnessAvg)         
        f.append(LA_Avg)
        f.append(LB_Avg)
        f.append(LC_Avg)
        img.close()     
        
        # compute the Laplacian of the image and then return the focus
        # measure, which is simply the variance of the Laplacian
        grayImg = cv2.imread(direct+"\\"+filename,0)
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        fm = cv2.Laplacian(grayImg, cv2.CV_64F).var()
  
        f.append(fm);
        

        
        im = np.array ((Image.open(direct+"\\"+filename)).convert('HSV'))
        

        # exposure of light and colourfulness

        f1 = 0

        im = misc.imread(direct+"\\"+filename)
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
        # WAVELET TRANSFORM
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

        coeffs = pywt.wavedec2(h, 'db1', level=3)
        cA3, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs


        #print str(cH3.shape) + str(cH2.shape) + str(cH1.shape

        # level1
        f10 = (np.sum(cH1) + np.sum(cV1) + np.sum(cD1))#/(np.nlinalg.det(cH1)+np.nlinalg.det(cV1)+np.nlinalg.det(cD1))

        # level2
        f11 = (np.sum(cH2) + np.sum(cV2) + np.sum(cD2))#/(np.linalg.det(cH2)+np.linalg.det(cV2)+np.linalg.det(cD2))

        # level3
        f12 = (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))#/(np.linalg.det(cH3)+np.linalg.det(cV3)+np.linalg.det(cD3))

        f.append(f10)
        f.append(f11)
        f.append(f12)


        # wavelet transform on saturation

        coeffs = pywt.wavedec2(s, 'db1', level=3)
        cA3, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs

        # level1
        f13 = (np.sum(cH1) + np.sum(cV1) + np.sum(cD1))#/(np.nlinalg.det(cH1)+np.nlinalg.det(cV1)+np.nlinalg.det(cD1))

        # level2
        f14 = (np.sum(cH2) + np.sum(cV2) + np.sum(cD2))#/(np.linalg.det(cH2)+np.linalg.det(cV2)+np.linalg.det(cD2))

        # level3
        f15 = (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))#/(np.linalg.det(cH3)+np.linalg.det(cV3)+np.linalg.det(cD3))

        f.append(f13)
        f.append(f14)
        f.append(f15)

        # wavelet transform on value

        coeffs = pywt.wavedec2(v, 'db1', level=3)
        cA3, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs

        # level1
        f16 = (np.sum(cH1) + np.sum(cV1) + np.sum(cD1))#/(np.nlinalg.det(cH1[0:cH1.shape[0]][0:])+np.nlinalg.det(cV1)+np.nlinalg.det(cD1))

        # level2
        f17 = (np.sum(cH2) + np.sum(cV2) + np.sum(cD2))#/(np.linalg.det(cH2)+np.linalg.det(cV2)+np.linalg.det(cD2))

        # level3
        f18 = (np.sum(cH3) + np.sum(cV3) + np.sum(cD3))#/(np.linalg.det(cH3)+np.linalg.det(cV3)+np.linalg.det(cD3))

        f.append(f16)
        f.append(f17)
        f.append(f18)

        x = int(X/4)
        y = int(Y/4)
        
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
        f.append(f53)
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
        f.append(f54)
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
        f.append(f55)
        #im.close();
        
        return f ;
##for i in range(0,len(f)) :
##  print ("f" + str(i+1) + " -> " + str(f[i]))
##temp=getFeatureVector('123.jpg')
##print(temp)
