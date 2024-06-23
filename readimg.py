import cv2

# read a photo
img = cv2.imread('colorcolor.jpg')

# change img size
# img = cv2.resize(img,(300,300))
# resize by multipy
img = cv2.resize(img,(0,0),fx=2,fy=2)
# show this img out
# (window name, photo that want to show)
cv2.imshow('img',img)
# img will wait for x m second
# 0 -> wait tilt press instruction to close
# 1000 -> wait 1000 ms then close also press instruction to close
cv2.waitKey(0)