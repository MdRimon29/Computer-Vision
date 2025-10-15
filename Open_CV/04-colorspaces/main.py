import os

import cv2

img_path = os.path.join('.','Open_CV/data', 'space_hub.webp')

img=cv2.imread(img_path)

img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('img', img)
cv2.imshow('img_gray',img_gray)
cv2.imshow("img_rgb",img_rgb)
cv2.imshow('img_hsv', img_hsv)

cv2.waitKey(0)