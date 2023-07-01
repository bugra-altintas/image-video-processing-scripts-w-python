import os
import cv2 as cv
for i in os.listdir("./rgbimages"):
    img = cv.imread("./rgbimages/"+i)

    greyscale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    cv.imwrite("./greyscaleimages/"+i,greyscale)




