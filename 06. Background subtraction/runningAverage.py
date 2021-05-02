import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# read the frame from the camera
_, frame = cap.read()

# converting data type to float32
averageValue = np.float32(frame)

while True:
    # read the frame from camera
    _, frame = cap.read()

    # accumulateWeighted used to update the running weights
    cv2.accumulateWeighted(frame, averageValue, 0.02)

    resultingFrame = cv2.convertScaleAbs(averageValue)

    cv2.imshow('Original Window', frame)
    cv2.imshow('averageValue', resultingFrame)

    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break

cap.release()
cv2.destroyAllWindows()