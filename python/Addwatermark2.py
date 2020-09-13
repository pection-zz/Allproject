import os
import sys

from PIL import Image

EXTS = ('.jpg', '.png')
path='/Users/pection/Documents/MN_Business/AddwatermarkProgram/images'
logo=Image.open('logo.png')
watermark = Image.open('WatermarkB5.png')
logoWidth = logo.width
logoHeight = logo.height
watermarkW=watermark.width
watermarkH=watermark.height
for filename in os.listdir(path):
    if any([filename.lower().endswith(ext) for ext in EXTS]) and filename != lgo:
        image = Image.open(path + '/' + filename)
        imageWidth = image.width
        imageHeight = image.height
        image.paste(logo, (0, 0), logo)
        image.paste(logo, (int(imageWidth - logoWidth)/2), int((imageHeight - logoHeight)/2)), logo)
        image.save(path + '/' + filename)
