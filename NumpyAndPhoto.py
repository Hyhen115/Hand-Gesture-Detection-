import random

import cv2
import numpy as np

# # read img
img = cv2.imread('colorcolor.jpg')

# # img is actually an array
# print(img.shape)
# G B R
# [
#     [[0,255,0],[255,0,0],[0,0,255]...700],
#     [[],[],[]...700],
#     [[],[],[]...700],
#     ...1015
# ]

# img = np.empty((300,300, 3), np.uint8)

for row in range(300):
    for col in range(img.shape[1]):
        # B G R
        img[row][col] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

# cut img
cv2.imshow('newImage', img[400:600, 400:600])
cv2.imshow('img', img)
cv2.waitKey(0)
