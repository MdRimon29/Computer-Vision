import os
import cv2

#read video
vdo_path=os.path.join('.','Open_CV/data', 'animal_walking.mp4')       # '.' means current directory.
video = cv2.VideoCapture(vdo_path)

#visualize video
ret=True

while ret:
    ret, frame=video.read()

    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(40)

video.release() #Closes the video file and releases resources.
cv2.destroyAllWindows() #Closes all OpenCV windows that were opened with cv2.imshow.

