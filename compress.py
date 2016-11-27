import numpy
import cv2
import sys
from cat_detector import getcats



    
imgname = sys.argv[1]
print(imgname)

img = cv2.imread(imgname)
avg_per_row = numpy.average(img, axis=0)
avg_colour = numpy.average(avg_per_row, axis=0)
avgcolour= [int(x) for x in avg_colour]
print(img.shape)
height, width = img.shape[:2]
print(height)
print(width)

objects = getcats(imgname) # Ilia's API. Return list of tuples (name , rect)     rect = [x,y,w,h]

# Write compressed file
basefilename = imgname.split('.')[0]
f = open ('{0}.pico'.format(basefilename), 'w')
f.write('{0}, {1}'.format(width, height) + '\n')
f.write('{0}\n'.format(avgcolour))
f.write('-----\n')

for o in objects:
    f.write('{0}\n'.format(o[0]))
    f.write('{0}\n'.format(o[1]))
    
f.close()

#[{'name':cat, 'rect':[x, y, w, h]}]

