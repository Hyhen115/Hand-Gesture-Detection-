import cv2

# save the vid to a variable
# cap = cv2.VideoCapture('thumb.mp4')

# save the camera vid
cap = cv2.VideoCapture(1)

# vid is a combination of many photos
# we need to show all photos in the video
while True:
    # ret -> bool for telling is getting next frame successful
    # frame -> if ret == true will obtain the next photo
    ret, frame = cap.read()

    # if have next frame
    if ret:
        # resize the video
        frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
        # show that frame
        cv2.imshow('video', frame)
    else:
        # when video stopped
        break
    # wait key is detecting input
    # if press key is q -> break
    if cv2.waitKey(10) == ord('q'):
        break



