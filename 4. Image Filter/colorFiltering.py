''' color filtering in live videos using color thresholding '''

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    cam, frame = cap.read()
    if cam is True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([30, 150, 50])
        upper_blue = np.array([255, 255, 180])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
