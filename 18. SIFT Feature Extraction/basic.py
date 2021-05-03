import numpy as np
import cv2

img = cv2.imread('./Media/apple.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

keypoints, descrptors = sift.detectAndCompute(img, None)
sift_image = cv2.drawKeypoints(gray_img, keypoints, img)

cv2.imshow('image', sift_image)

k = cv2.waitKey(0) & 0xff

if k == 27:
    cv2.destroyAllWindows()