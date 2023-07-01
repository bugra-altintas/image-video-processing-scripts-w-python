import cv2
import os

for i in os.listdir('.'):
    img = cv2.imread(i)
    name = i.split(".")
    if(name[1] == "jpeg"):
        os.remove(i)
        cv2.imwrite(name[0]+".png",img)
    