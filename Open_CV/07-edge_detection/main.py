import os

import cv2
import numpy as np


img=cv2.imread(os.path.join('.','Open_CV/data','messi.webp'))

img_edge = cv2.Canny(img, 80, 250)


# Both dilate and erode are morphological operations applied to binary images (like edge images from Canny).
# Morphological operations use a small matrix called a kernel (or structuring element) to modify the shapes in the image.

img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))   # make edges thicker

img_edge_e = cv2.erode(img_edge, np.ones((3, 3), dtype=np.int8))  # make edges thinner

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)