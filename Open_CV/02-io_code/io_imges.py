import os
import cv2

#image read
image_path=os.path.join('.','Open_CV/data','space_hub.webp')

img = cv2.imread(image_path)

#image write
img_path=os.path.join('.','data','space_hub_write.jpg')
cv2.imwrite(img_path,img)

#image visualize
cv2.imshow('image',img)
cv2.waitKey(0)     # This function waits for a key press from keyboard 
                    # e.g., cv2.waitKey(5000), it will wait for 5000 milliseconds (5 seconds)