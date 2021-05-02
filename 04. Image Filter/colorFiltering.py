''' color filtering in live videos using color thresholding '''

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    cam, frame = cap.read()
    if cam is True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([101,50,38])
        upper_blue = np.array([110,255,255])

        lower_red = np.array([160,20,70])
        upper_red = np.array([190,255,255])

        lower_green = np.array([36, 25, 25])
        upper_green = np.array([86, 255,255])

        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        res_red = cv2.bitwise_and(frame, frame, mask=mask_red)

        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        res_green = cv2.bitwise_and(frame, frame, mask=mask_green)

        cv2.imshow('frame', frame)
        cv2.imshow('Blue', res_blue)
        cv2.imshow('Red', res_red)
        cv2.imshow('green', res_green)
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
