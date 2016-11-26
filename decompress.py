import sys
from PIL import Image

#filename = sys.argv[1]
filename = 'C:\Users\Sony\Desktop\TerribleHacks\piltest.txt'
path_to_images = 'C:\Users\Sony\Desktop\TerribleHacks\Images'

f = open(filename)
lines = f.read().split('\n')
f.close()

# Read image properties
imgsize = [ int (x) for x in lines[0].split(',') ]
imgcolor = lines[1]

# Read in objects from file
objects = []

i = 0
for line in lines[3:]:
    if i == 0:
        o = {}
        o['name'] = line
    elif i == 1:
        o['pos'] = line.split(',')
    elif i == 2:
        o['size'] = line.split(',')
        objects.append(o)
        i = -1
    i += 1

print (imgsize)
print (imgcolor)
print (objects)

# Build image
im = Image.new('RGBA', imgsize, imgcolor)
im.format = "PNG"

for o in objects:
    ofilename = "{0}\{1}.png".format(path_to_images, o['name'])
    print (ofilename)
    oimg = Image.open(ofilename)
    objx, objy = int(o['pos'][0]), int(o['pos'][1])
    objwidth, objheight = int(o['size'][0]), int(o['size'][1])
    oimg = oimg.resize((objwidth, objheight))
    region = (objx, objy, objx + objwidth, objy + objheight)
    
    im.paste(oimg, region, oimg)
    
im.show()
