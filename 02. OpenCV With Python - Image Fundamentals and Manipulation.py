# import library
import cv2
import random

# load the image
img = cv2.imread('assets/apple.jpg', -1)

# print the image
print(img)

# type of img
print(type(img))

# shape of img
print(img.shape)

# first roll in img
print(img[0])

# copy image
tag = img[500:700, 300:600]
img[100:300, 550:850] = tag

# display the image
cv2.imshow('Image', img)

# wait time after image is loaded '0' = infinity, '10' = 10 seconds
cv2.waitKey(0)

# to distroy all windows
cv2.destroyAllWindows()