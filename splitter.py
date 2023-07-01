import cv2
import sys

video_path=sys.argv[1]

capture = cv2.VideoCapture(video_path)
fps = round(capture.get(cv2.CAP_PROP_FPS))
print(fps)
frameNr = 0
 

 # split the video to frames with 1 fps
while (True):
 
    success, frame = capture.read()
 
    if success:
        if frameNr % fps == 0:
            if frameNr//fps<10:
                cv2.imwrite(f'/Users/bugra/Desktop/frames-new2/00000{frameNr//fps}.png', frame)
            elif frameNr//fps<100:
                cv2.imwrite(f'/Users/bugra/Desktop/frames-new2/0000{frameNr//fps}.png', frame)
            else:
                cv2.imwrite(f'/Users/bugra/Desktop/frames-new2/000{frameNr//fps}.png', frame)
            print("writing image",frameNr//fps)
    else:
        break
   
    frameNr = frameNr+1
 
capture.release()