import cv2 as cv
import os
import sys

def adaptive_histogram_equalization(img):
    # may change clipLimit to a lower val
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(img)


video_path = sys.argv[1]

cap = cv.VideoCapture(video_path)
success = True
width  = int(cap.get(3))  # float `width`
height = int(cap.get(4))  # float `height`
writer = cv.VideoWriter('equalized.avi',cv.VideoWriter_fourcc('M','J','P','G'),cv.CAP_PROP_FPS,(width,height))
while cap.isOpened() and success:
    
    success, frame = cap.read()

    if success:
        print("reading frame..")
        greyscale = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        frame_eq = adaptive_histogram_equalization(greyscale)
        writer.write(frame_eq)

cap.release()
writer.release()

    
