import sys
from PIL import Image

filename = sys.argv[1]
path_to_images = 'Images'

f = open(filename)
lines = f.read().split('\n')
print(lines)
f.close()

# Read image properties
imgsize = [ int (x) for x in lines[0].split(',') ]
imgcolor = lines[1]

# Read in objects from file
objects = []

i = 0
for line in lines[3:]:
    if i == 0:
        o = []
        o.append(line)
    elif i == 1:
        o.append(line)
        objects.append(o)
        i = -1
    i += 1

# Build image
#im = Image.new('RGBA', imgsize, imgcolor)
im = Image.new('RGBA', imgsize, "white")
im.format = "PNG"

print(objects)

for o in objects:
    print(o)
    ofilename = "{0}/{1}.png".format(path_to_images, o[0])
    oimg = Image.open(ofilename)
    rect = o[1].replace('[', '').replace(']', '').split()
    objx, objy = int(rect[0]), int(rect[1])
    objwidth, objheight = int(rect[2]), int(rect[3])
    oimg = oimg.resize((objwidth, objheight))
    region = (objx, objy, objx + objwidth, objy + objheight)
    im.paste(oimg, region, oimg)
    
im.show()