import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('../Media/face-001.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for face in faces:
    x, y, width, height = face
    # draw a rectangle for detection
    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 1)

cv2.imshow('Face Detection',img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('../Media/face-detected.jpeg', img)
    cv2.destroyAllWindows()