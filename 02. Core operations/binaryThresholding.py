import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./Media/bnw.jfif')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

plt.imshow(th1, 'gray')
plt.title('Binary Thresholding')
plt.xticks([])
plt.yticks([])
plt.show()