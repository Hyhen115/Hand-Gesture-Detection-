from unittest import result

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
handLmsStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=10)
handConStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=5)
pTime = 0
cTime = 0

touching = False

while True:
    ret, img = cap.read()
    if ret:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        imgHeight = img.shape[0]
        imgWidth = img.shape[1]
        # if have hands
        if result.multi_hand_landmarks:
            # for each hand
            for handLms in result.multi_hand_landmarks:
                # draw all connections and dots out
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, handLmsStyle, handConStyle)
                # loop through all fingermarks
                for i, lm in enumerate(handLms.landmark):
                    # x coordinates
                    xPos = int(lm.x * imgWidth)
                    # y coordinates
                    yPos = int(lm.y * imgHeight)
                    # put coordinates besides the circles
                    cv2.putText(img, str(i), (xPos-25, yPos+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255,255,255),2)
                    # when is the fingertip points
                    if i == 4 or i == 8 or i == 12 or i == 16 or i == 20:
                        # bigger circle and color
                        cv2.circle(img, (xPos, yPos), 15, (0, 242, 255),cv2.FILLED)
                    # print the point position
                    print(i, xPos, yPos)

        # set fps
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv2.putText(img, f"FPS : {int(fps)}", (30,50),cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255),2)

        cv2.imshow('img', img)

    if cv2.waitKey(1) == ord('q'):
        break
