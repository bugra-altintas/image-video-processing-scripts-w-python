import os
import cv2 as cv
import sys

def adaptive_histogram_equalization(img):
    # may change clipLimit to a lower val
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(img)

folder = sys.argv[1]

for i in os.listdir(folder):
    img = cv.imread(folder+'/'+i)

    greyscale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img_eq = adaptive_histogram_equalization(greyscale)

    cv.imwrite(folder+"_eq"+'/'+i,img_eq)
