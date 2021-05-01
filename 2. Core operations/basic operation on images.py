import numpy as np
import cv2
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]

img1 =  cv2.imread("./Media/opencv-logo-white.png")

replicate = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value= BLUE)

plt.subplot(321),plt.imshow(img1, 'gray'),plt.title('original')
plt.subplot(322),plt.imshow(replicate, 'gray'),plt.title('replicate')
plt.subplot(323),plt.imshow(reflect, 'gray'),plt.title('reflect')
plt.subplot(324),plt.imshow(reflect101, 'gray'),plt.title('reflect101')
plt.subplot(325),plt.imshow(wrap, 'gray'),plt.title('wrap')
plt.subplot(326),plt.imshow(constant, 'gray'),plt.title('constant')

plt.show()