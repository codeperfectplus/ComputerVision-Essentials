""" Live Background subtraction using opencv """

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()
    if ret:    
        fgmask = fgbg.apply(frame)
        
        cv2.imshow('frame', fgmask)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()