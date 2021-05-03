""" Face detection using deep learning and opencv """
import numpy as np
import cv2

# Global Declarations
# https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt
prototxt_path = "./assets/deploy.prototxt.txt"
# https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20180205_fp16/res10_300x300_ssd_iter_140000_fp16.caffemodel 
model_path = "./assets/res10_300x300_ssd_iter_140000.caffemodel"

confThresh=0.8
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

def detectFace(imgPath):
    img = cv2.imread(imgPath)

    (h, w) = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))
    
    net.setInput(blob)
    detections = net.forward()
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence < confThresh:
            continue

        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(img, (startX, startY), (endX, endY),(0, 0, 255), 2)
        
    cv2.imshow("Output", img)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()
    elif key == ord('s'):
        cv2.imwrite('./Media/face-detected-dnn.jpeg', img)
        cv2.destroyAllWindows()



path_img = './Media/face-001.jpg'
detectFace(path_img)
