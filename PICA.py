# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:25:52 2016

@author: Ilia
"""

import cv2
from PIL import Image
import os

img_dirs=['Apple_logo', 'Balloons', 'Chair', 'Elon_Musk', 'iPhone', 'Pancakes', 'Pepe', 'Pepsican', 'Water_bottle']

def get_image_list(directory):
    contents = os.listdir(directory)
    return contents
def get_contours(filepath, show):
    #reading the image 
    image = cv2.imread(filepath)
    edged = cv2.Canny(image, 10, 250)
    if show:
        cv2.imshow("Edges", edged)
        cv2.waitKey(0)
     
    #applying closing function 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    if show:
        cv2.imshow("Closed", closed)
        cv2.waitKey(0)
     
    #finding_contours 
    (_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return cnts
def show_contours(filepath,cnts):
    image = cv2.imread(filepath)
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
    cv2.imshow("Output", image)
    cv2.waitKey(0)
def crop_contours(idy,filepath,cnts,width,height):
    idx=0
    image = cv2.imread(filepath)
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w>width/20 and w<width/2 and h>height/5:
            idx+=1
            new_img=image[y:y+h,x:x+w]
            cv2.imwrite("contours/"+str(idy)+"_"+str(idx) + '.jpg', new_img)
def run_contours(filepath,idy):
    im=Image.open(filepath)
    width,height=im.size
    im.close()
    contours = get_contours(filepath,False)
    #show_contours(filepath,contours)
    crop_contours(idy,filepath,contours,width,height)
idy = 0
for filepath in get_image_list("photos"):
    idy+=1
    run_contours("photos/"+filepath,idy)   