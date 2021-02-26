''' Real time Face bluring using webcam '''

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_color = frame[y:y+h, x:x+w]
        roi_color = cv2.GaussianBlur(roi_color, (23, 23), 30)
        frame[y: y+h, x: x+w] = roi_color

    cv2.imshow('bluredFace', frame)
    if cv2.waitKey(30) & 0xff == ord("q"):
        break
    

cap.release()
cv2.destroyAllWindows()