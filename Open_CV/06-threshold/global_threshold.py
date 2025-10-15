import os
import cv2

img=cv2.imread(os.path.join('.','Open_CV/data','bear.jpg'))

img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thres= cv2.threshold(img_gray,80,255, cv2.THRESH_BINARY)

thres = cv2.blur(thres,(7,7))
ret, thres= cv2.threshold(thres,80,255, cv2.THRESH_BINARY)

cv2.imshow('image',img)
cv2.imshow('img_gray',img_gray)
cv2.imshow('img_thres',thres)

cv2.waitKey(0)