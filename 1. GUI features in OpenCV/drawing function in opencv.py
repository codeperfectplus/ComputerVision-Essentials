import cv2  # python-opencv
import numpy as np

width, height = 800, 600
x1, y1 = 0, 0
x2, y2 = 200, 400
image = np.ones((height, width)) * 255

line_thickness = 2
cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), thickness=line_thickness)