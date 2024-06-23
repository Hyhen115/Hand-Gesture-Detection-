import cv2
import numpy as np

# get vid
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        cv2.imshow('frame', frame)
        cv2.waitKey(1)
    else:
        break