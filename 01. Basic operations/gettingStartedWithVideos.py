''' Getting started with Videos in Opencv'''
import cv2

cap = cv2.VideoCapture(0)

while True:
    # capture frame by frame
    check, frame = cap.read()
    if check:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # display the result
        cv2.imshow('frame', gray)

        # break the while loop by 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#release the cap
cap.release()
cv2.destroyAllWindows()
