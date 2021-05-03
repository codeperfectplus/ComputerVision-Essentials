""" Real time Edge detection """
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    check, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if check:
        # applying canny edge transformation
        edges = cv2.Canny(gray, threshold1=30, threshold2=100)

        # showing the output frame
        cv2.imshow('Original',frame)
        cv2.imshow('Edges', edges)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
