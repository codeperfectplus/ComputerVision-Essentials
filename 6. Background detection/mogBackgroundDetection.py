""" Background subtraction using opencv """

import numpy as np
import cv2

cap = cv2.VideoCapture('./Media/people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    
    cv2.imshow('frame', fgmask)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()