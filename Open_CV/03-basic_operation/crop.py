import os

import cv2

img = cv2.imread(os.path.join('.','Open_CV/data','space_hub.webp'))

print(img.shape)

cropped_img = img[100:540, 100:540]

cv2.imshow('image', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)