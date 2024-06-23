import cv2
import numpy as np

kernel = np.ones((3,3), np.uint8)

# read img
img = cv2.imread('colorcolor.jpg')
# resize
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

# convert img to gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# convert to blur
blur = cv2.GaussianBlur(img,(3,3),0)

# convert to canny (only edges)
# (lowest limit, highest limit)
canny = cv2.Canny(img,100,150)

# convert to dilate (make edge thick)
dilated = cv2.dilate(canny,kernel,iterations=2)

# convert to eroded (make edge thinner)
eroded = cv2.erode(dilated,kernel,iterations=4)

# show img
cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.imshow('dilated',dilated)
cv2.imshow('eroded',eroded)
cv2.waitKey(0)