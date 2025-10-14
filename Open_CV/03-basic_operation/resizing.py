import os
import cv2

image_path=os.path.join('.','Open_CV/data','space_hub.webp')
img = cv2.imread(image_path)

print(img.shape)

resized_img = cv2.resize(img,(500,500))

print(resized_img.shape)

cv2.imshow('img',img)
cv2.imshow('resized_img',resized_img)
cv2.waitKey(0)