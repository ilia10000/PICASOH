import numpy
import cv2
import sys

def getavgcolour(imgname):
    img = cv2.imread(imgname)
    avg_per_row = numpy.average(img, axis=0)
    avg_colour = numpy.average(avg_per_row, axis=0)
    return [int(x) for x in avg_colour]
    
imgname = sys.argv[0]

objects = getcats() # Ilia's API. Return list of dictionaries {name: , rect: []}  

avgcolour = getavgcolour(imgname)
height, width = img.shape

# Write compressed file
basefilename = imgname.split('.')[0]
f = open ('{0}.pico'.format(basefilename))
f.write('{0}, {1}'.format(width, height) + '\n')
f.write(avgcolour + '\n')
f.write('-----')

for o in objects:
    f.write(o['name'] + '\n')
    f.write(o['rect'] + '\n')
    
f.close()

#[{'name':cat, 'rect':[x, y, w, h]}]

