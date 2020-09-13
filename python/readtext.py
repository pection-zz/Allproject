from langdetect import detect
import cv2
import pytesseract
import argparse
import imutils
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", type=str,
# 	help="path to input image")
# args = vars(ap.parse_args())

pytesseract.pytesseract.tesseract_cmd =  '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
# if args["image"] !=False:
	# print (args["image"])
img = cv2.imread("location.png")
# img = imutils.resize(img,width=600)
# custom_config = r'--oem 3 --psm 6 outputbase digits'
# print(pytesseract.image_to_string(img, lang='tha',config=custom_config))
custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6'
print(pytesseract.image_to_string(img,  lang='tha',config=custom_config))

text = pytesseract.image_to_string(Img.open(filename),lang='tha')
text = text.replace(' ','')
print (text)
