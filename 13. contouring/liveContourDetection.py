""" Live cam contouring using thresholding and findContours() """

import cv2

cap = cv2.VideoCapture(0)

while True:
    cam, frame = cap.read()

    if cam is True:
        # convert frame into grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # create a binary threshold
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, 
                                               cv2.CHAIN_APPROX_SIMPLE)

        image = cv2.drawContours(image=frame, contours= contours,
                                contourIdx=-1, color=(128, 0, 0), thickness=2)

        cv2.imshow("live-contour-detector", image)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
