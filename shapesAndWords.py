import cv2
import numpy as np

# all black img
img = np.zeros((600,600,3), np.uint8,)

# draw line pt1 to pt2
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0),3)

# draw square line from pt1 to pt2
cv2.rectangle(img, (0,0), (img.shape[1],img.shape[0]), (0,0,255),10)

# draw square filled
cv2.rectangle(img, (0,0), (400,300), (255,255,0),cv2.FILLED)

# draw circle
cv2.circle(img, (300,400), 30, color=(0,255,255), thickness=-1)

# draw words
cv2.putText(img,'Hello',(100, 500), cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),2)
# show img
cv2.imshow('img',img)
cv2.waitKey(0)
