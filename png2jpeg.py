import os
import sys
import cv2 as cv



count = len(sys.argv)
for i in range(1,count):
    img_path = sys.argv[i]
    name = img_path.split('/')[-1]
    name = name.split('.')[0]
    img_parent = img_path.split('/')[0:-1]
    img_jpeg='/'.join(img_parent) + "/" + name + ".jpg"
    print(img_parent)
    img = cv.imread(img_path)
    cv.imwrite(img_jpeg,img)



