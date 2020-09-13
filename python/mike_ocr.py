import cv2
import glob
cv_img = []
for img in glob.glob("/Users/pection/Documents/Programing/Addwatermark/*."):
    n= cv2.imread(img)
    cv_img.append(n)

print (len(cv_img))