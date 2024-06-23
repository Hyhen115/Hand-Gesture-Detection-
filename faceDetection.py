import cv2

img = cv2.imread('lenna.jpg')
# change to gray img
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# load the model for face detection
faceCascade = cv2.CascadeClassifier('face_detect.xml')
# detect the gray photo's face
faceRect = faceCascade.detectMultiScale(gray, 1.1, 5)
print(len(faceRect))

for (x,y,w,h) in faceRect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img', img)
cv2.waitKey(0)