import cv2
import sys

video_path=sys.argv[1]

vidcap = cv2.VideoCapture(video_path)

success,image = vidcap.read()
count = 0
index = 0
while success:
  success, image = vidcap.read()
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*20000))
  cv2.imwrite("/Users/bugra/Desktop/frames-new/%06d.png" % count, image)  
  print('Read a new frame: ', success)
  count += 1