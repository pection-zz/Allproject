from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import cv2
import glob
import numpy as np 
cv_img = []

number = 1
# org 
org = (0, 10) 
  
# fontScale 
fontScale = 1
   
# Blue color in BGR 
color = (0, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2   
# print("asd") 
for img in glob.glob("/Users/pection/Documents/FastFurniture/Files/png/*.png"):
    n= cv2.imread(img)
    name = "Product No. "+ str(number)
    print(type(n))
    print (name,img,n)
    font = cv2.FONT_HERSHEY_SIMPLEX 
    image = cv2.putText(img,name,org , font, fontScale, color, thickness, cv2.LINE_AA)
    number+=1
    cv2.imshow("ASD",image)
    cv2.waitKey(0)
    print("HIHIHI")
    cv2.imwrite('/Users/pection/Documents/FastFurniture/Files/watermark/category_'+number+'.png',image)
    cv_img.append(n)


                