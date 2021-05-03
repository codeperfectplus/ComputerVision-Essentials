""" Common object detection using CvLib and yolo3 """

import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

img = cv2.imread('./Media/apple.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bbox, label, conf = cv.detect_common_objects(gray)

output_image = draw_bbox(im, bbox, label, conf)

plt.imshow(output_image)
plt.savefig("./Media/apple-detected.jpeg")
plt.show()