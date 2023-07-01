import cv2
import sys

img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])

#find name of img1
img1_name = sys.argv[1].split('/')[-1]

#find difference between img1 and img2
diff = cv2.absdiff(img1, img2)
#writing the difference to a file
cv2.imwrite(f'/Users/bugra/Desktop/{img1_name}', diff)

