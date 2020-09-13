import os
import sys
import numpy as np
from PIL import Image
import imutils
import cv2
def checkimagesize(image):
    (imageWidth , imageHeight)=image.shape[:2]
    print (imageWidth,imageHeight)
    if imageWidth>960:
        imageWr=imutils.resize(image,width=960)
    return imageWr
watermark = cv2.imread('/Users/pection/Documents/mn_furniture/AddwatermarkProgram/WatermarkB5.png',-1)
imageWr=imutils.resize(watermark,width=300)
cv2.imwrite('/Users/pection/Documents/mn_furniture/AddwatermarkProgram/WatermarkB3.png',imageWr)
# cv2.imshow("Hi",imageresize)

