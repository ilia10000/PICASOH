import cv2
import numpy



def getavgcolour(imgname):
    img = cv2.imread(imgname)
    avg_per_row = numpy.average(img, axis=0)
    avg_colour = numpy.average(avg_per_row, axis=0)
    return [int(x) for x in avg_colour]
    
    
a=getavgcolour('Images/pepe.png')