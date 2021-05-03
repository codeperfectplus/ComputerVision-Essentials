import numpy as np
import cv2

cap = cv2.VideoCapture('motion.avi')

ret, frame = cap.read()
gs_im0 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
points_prev = cv2.goodFeaturesToTrack(gs_im0, 100, 0.03, 9.0, False)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    gs_im1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Call tracker.
    points, st, err = cv2.calcOpticalFlowPyrLK(gs_im0, gs_im1, points_prev, None, (3,3))

    for i,p in enumerate(points):
        a,b = p.ravel()
        frame = cv2.circle(frame,(a,b),3,(255,255,255),-1)

    cv2.imshow('frame',frame)
    points_prev = points
    gs_im0 = gs_im1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()