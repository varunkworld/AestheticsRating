##### COLOR AVERAGING #####
import PIL
from PIL import Image 
import sys
import numbers

#direct= path to the dataset directory
direct='K:\Old\E_DRIVE\ACADEMICS IV\BTP\April\FE\Pydownloaded'

##### Function to compute Avg RGB values

def ImgAnalyze( str ):
        ##str=str(filename.ext)
        
        # open the image
        img = Image.open(direct+"\\"+str)    #file = open(direct+"\\"+str, "r")


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
                    
                # compute average RGB values
                rAvg = r/counter
                gAvg = g/counter
                bAvg = b/counter

                #you can also return rounded values upto required precision using round
                img.close()
                return (rAvg, gAvg, bAvg)


############ Function Defination  End ###############


############## Demonstration
#print(ImgAnalyze('123.jpg'),sep='   ');


