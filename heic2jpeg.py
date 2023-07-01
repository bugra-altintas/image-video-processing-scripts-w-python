import os
import cv2
import sys


path = "/Users/bugra/Desktop/IMG_1766.HEIC"
#read image
img = cv2.imread("/Users/bugra/Desktop/IMG_1766.HEIC")

name = "IMG_1766.jpg"

cv2.imshow(name,img)
cv2.waitKey(0)

cv2.imwrite(name,img)