import cv2

# vid
cap = cv2.VideoCapture(1)

# load the model for face detection
faceCascade = cv2.CascadeClassifier('face_detect.xml')


while True:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # detect the gray photo's face
        faceRect = faceCascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faceRect:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, 'face', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.imshow('Video', img)
        cv2.waitKey(1)