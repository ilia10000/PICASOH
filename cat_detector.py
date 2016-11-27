# USAGE
# python cat_detector.py --image images/cat_01.jpg

# import the necessary packages
import argparse
import cv2
def getcats(im):
    # load the input image and convert it to grayscale
    image = cv2.imread(im)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # load the cat detector Haar cascade, then detect cat faces
    # in the input image
    detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
    rects = detector.detectMultiScale(gray, scaleFactor=1.3,
    	minNeighbors=10, minSize=(75, 75))
    
    final = [("cat",rect) for rect in rects]
    
    # loop over the cat faces and draw a rectangle surrounding each
    for (i, (x, y, w, h)) in enumerate(rects):
    	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    	cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
    		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
    
    # show the detected cat faces
    cv2.imshow("Cat Faces", image)
    cv2.waitKey(0)
    return final