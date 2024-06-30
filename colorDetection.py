import cv2
import numpy as np

#function empty
def empty(v):
    pass

img = cv2.imread('colourDet.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

# add a window to control the hsv stats
cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar',640,320)

# create different track bars x 6
cv2.createTrackbar('Hue Min','TrackBar',0,179,empty)
cv2.createTrackbar('Hue Max','TrackBar',179,179,empty)
cv2.createTrackbar('Sat Min','TrackBar',0,255,empty)
cv2.createTrackbar('Sat Max','TrackBar',255,255,empty)
cv2.createTrackbar('Val Min','TrackBar',0,255,empty)
cv2.createTrackbar('Val Max','TrackBar',255,255,empty)

# change to hsv
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# get value for the track bar
while True:
    h_min = cv2.getTrackbarPos('Hue Min','TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max','TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min','TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max','TrackBar')
    v_min = cv2.getTrackbarPos('Val Min','TrackBar')
    v_max = cv2.getTrackbarPos('Val Max','TrackBar')
    # print values
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    # create 2 array for all 3 stats for lower and upper
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    # filter out the color
    mask = cv2.inRange(hsv,lower,upper)
    # do bitwise and on mask img and img so will filter out the white part
    result = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    # every frame stay
    cv2.waitKey(1)
