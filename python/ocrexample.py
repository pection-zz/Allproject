import imutils
# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
pytesseract.pytesseract.tesseract_cmd =  '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
image2=image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename),lang='tha')
os.remove(filename)
text= text.replace(' ', '')

# show the output images
# cv2.imshow("Image",imutils.resize(image, width=800))
# cv2.imshow("Output",imutils.resize(gray, width=800))
# cv2.waitKey(0)
