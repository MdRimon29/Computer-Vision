"""
But unlike simple thresholding, adaptive thresholding computes the threshold locally for each small region instead of using a single global value.

This is especially useful for uneven lighting — like handwritten text, scanned documents, or shadows.
"""


import os
import cv2

img=cv2.imread(os.path.join('.','Open_CV/data','handwritten.png'))

img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 20)
ret, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('image',img)
cv2.imshow('img_gray',img_gray)
cv2.imshow('simple_thresh',simple_thresh)
cv2.imshow('adaptive_thresh',adaptive_thresh)

cv2.waitKey(0)