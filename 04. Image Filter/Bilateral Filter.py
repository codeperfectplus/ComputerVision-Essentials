'''
OpenCV provides the bilateralFilter() function to apply the bilateral filter on the image. The bilateral filter can reduce unwanted noise very 
well while keeping edges sharp. The syntax of the function is given below

src- It denotes the source of the image. It can be an 8-bit or floating-point, 1-channel image.
dst- It denotes the destination image of the same size. Its type will be the same as the src image.
d - It denotes the diameter of the pixel neighborhood (integer type) that is used during filtering. If its value is negative, then it is computed from sigmaSpace.
sigmaColor - It denotes the filter sigma in the color space.
sigmaSpace - It denotes the filter sigma in the coordinate space.
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./Media/sample.jpeg',1)

blur = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Bilateral Filter')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()