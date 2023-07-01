import cv2 as cv
import sys
import math
import matplotlib.pyplot as plt
import random
import time
import numpy as np
def adaptive_histogram_equalization(img):
    # may change clipLimit to a lower val
    clahe = cv.createCLAHE(clipLimit=10, tileGridSize=(8,8))
    return clahe.apply(img)

def crop_rect(img, rect):
    # get the parameter of the small rectangle
    center, size, angle = rect[0], rect[1], rect[2]
    center, size = tuple(map(int, center)), tuple(map(int, size))

    # get row and col num in img
    height, width = img.shape[0], img.shape[1]

    # calculate the rotation matrix
    M = cv.getRotationMatrix2D(center, angle, 1)
    # rotate the original image
    img_rot = cv.warpAffine(img, M, (width, height))

    # now rotated rectangle becomes vertical, and we crop it
    img_crop = cv.getRectSubPix(img_rot, size, center)

    return img_crop, img_rot

def detect_stripe(img):
    edges = cv.Canny(img, 50, 150)

    # Apply Hough line transform
    lines = cv.HoughLines(edges, 1, np.pi/180, 100)

    # Select the lines that correspond to stripes
    stripes = []
    for line in lines:
        rho, theta = line[0]
        if np.abs(theta) > np.pi/4 and np.abs(theta) < 3*np.pi/4:
            x1 = 0
            y1 = int(rho / np.sin(theta))
            x2 = img.shape[1]
            y2 = int((rho - img.shape[1]*np.cos(theta)) / np.sin(theta))
            if y1 != y2:
                slope = (x2-x1)/(y2-y1)
                if np.abs(slope) > 1.5:
                    stripes.append(line)

    # Draw the detected stripes on the original image
    for line in stripes:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv.line(img, (x1,y1), (x2,y2), (0,0,255), 2)
    return img

def extract_edges(img2):
    rect = cv.minAreaRect(cont)
    box = cv.boxPoints(rect)
    box = np.intp(box)
    cv.drawContours(img2,[box],0,(0,255,255),2)
    #cv.drawContours(img2,[hull],contourIdx=-1,thickness=5,color=(255,0,0))

    img_crop, img_rot = crop_rect(img2,rect)
    cv.imshow("approx",img2)
    cv.waitKey(0)

    #cv.imshow("edges",edges)
    print(img_crop.shape)

    cv.imwrite("../1_crop.png",img_crop)

    #img_crop = cv.bitwise_not(img_crop) 

    #cv.imwrite("../1_crop_not.png",img_crop)

    ret2 , thresh2 = cv.threshold(img2, 180, 255, cv.THRESH_BINARY)

    cv.imwrite("../1_thresh.png",thresh2)

    #cv.imshow("crop_thresh",thresh2)
    #cv.waitKey(0)

    edges = cv.Canny(thresh2,50,150)
    #cv.imshow("edges",edges)

    cv.imwrite("../1_crop_edges.png",edges)

# Read image
img = cv.imread(sys.argv[1])
# extract histogram
hist = cv.calcHist([img], [0], None, [256], [0, 256])

#convert to greyscale
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Image", img)
cv.waitKey(0)

#plot histogram
#plt.plot(hist)
#plt.show()
"""res = None

res = cv.inRange(img,80,120)

cv.imshow("interval",res)
cv.waitKey(0)"""

ret , thresh = cv.threshold(img, 150, 255, cv.THRESH_BINARY)

cv.imshow("Image", thresh)
cv.waitKey(0)

folder = "örnek/"
num = "tombiş_"


#cv.imwrite(folder + num+ "thresh.jpg", thresh)

#cv.imwrite("thresh.jpg", thresh)

# Create kernel with kernel size
dilation_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (11,7))
erosion_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,3))

# Erode the image
eroded = cv.erode(thresh, erosion_kernel, iterations=1)

#cv.imwrite(folder + num+ "eroded.jpg", eroded)

# Dilate the eroded image
dilated = cv.dilate(eroded, dilation_kernel, iterations=2)

#cv.imwrite(folder + num+ "dilated.jpg", dilated)

contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

cont = max(contours,key=cv.contourArea)

ellipse = cv.fitEllipse(cont)

"""epsilon = 0.001*cv.arcLength(cont,True)
print(epsilon)
approx = cv.approxPolyDP(cont,epsilon,True)"""
#hull = cv.convexHull(cont,False)

extract_edges(img)

#draw largest line in the center of ellipse
angle = math.radians(ellipse[2])
center = (int(ellipse[0][0]), int(ellipse[0][1]))


# rotate point around center
def rotate_point(point, center, angle):
    x = point[0] - center[0]
    y = point[1] - center[1]
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return (int(new_x + center[0]), int(new_y + center[1]))

newp = rotate_point((int(ellipse[0][0]), int(ellipse[0][1]) + int(ellipse[1][1])/2), center, angle)
newp2 = rotate_point((int(ellipse[0][0]), int(ellipse[0][1]) - int(ellipse[1][1])/2), center, angle)


img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

random.seed(time.time())
if random.randint(0,1) == 0:
    cv.arrowedLine(img, center, newp, (0, 255, 0), 2,tipLength=0.25)
    cv.line(img, center, newp2, (0, 255, 0), 2)
else:
    cv.arrowedLine(img, center, newp2, (0, 255, 0), 2,tipLength=0.25)
    cv.line(img, center, newp, (0, 255, 0), 2)


#cv.arrowedLine(img, center, newp2, (0, 255, 0), 2)
#cv.line(img, center, newp, (0, 255, 0), 2)
cv.ellipse(img, ellipse, (0,0,255), 2)
cv.putText(img, "Angle: " + "%.2f" % ellipse[2], (10, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv.LINE_AA)
#img_contours = cv.drawContours(image=img, contours=contours, contourIdx=-1, color=(255,0,0), thickness=2)

#cv.imwrite(folder + num+ "res.jpg", img)

#cv.imwrite("dilated.jpg", dilated)
cv.imshow("Image", eroded)
cv.waitKey(0)

#cv.imshow("Image", dilated)
#cv.waitKey(0)

cv.imshow("Image", img)
cv.waitKey(0)
