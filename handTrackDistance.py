import cv2
import numpy as np
import time
import HandTrackingModule

#####################
wCam, hCam = 640, 480
#####################

# vid
cap = cv2.VideoCapture(1)

cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0


while True:
    success, img = cap.read()

    # calculate fps
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS : {int(fps)}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow('img', img)
    cv2.waitKey(1)