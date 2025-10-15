# blurring image means take an average of every single pixel around the pixel we want to see blur.

import os
import cv2

img = cv2.imread(os.path.join('.','Open_CV/data', 'cow-salt-peper.png'))

k_size=11   #here k_size means kernal size. 11 means 11*11 matrix,so 121 pixel from neighbour

img_blur=cv2.blur(img,(k_size,k_size))
img_gaussian_blur=cv2.GaussianBlur(img, (k_size,k_size), 5) # here 5 is sigma value. smaller means sharp Gaussian peak and bigger means flatter Gaussian curve
img_median_blur=cv2.medianBlur(img,k_size, 5)   # here one k_size, because medianBlur always makes squares window, so it takes just one k_size.

cv2.imshow('img',img)
cv2.imshow('img_blur',img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)

cv2.waitKey(0)