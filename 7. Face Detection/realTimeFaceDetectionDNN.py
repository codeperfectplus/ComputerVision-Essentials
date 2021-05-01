""" Real time face detection using deep learning """

import numpy as np
import cv2

proto='./deploy.prototxt.txt'
model='./res10_300x300_ssd_iter_140000.caffemodel'
confThresh=0.5
net = cv2.dnn.readNetFromCaffe(proto, model)

cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    frame=cv2.flip(frame,1)
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))
    
    net.setInput(blob)
    detections = net.forward()
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence < confThresh:
            continue

        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),(0, 0, 255), 2)
        
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()