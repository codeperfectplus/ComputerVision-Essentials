""" Image Resizing

- cv2.INTER_AREA: This is used when we need to shrink an image.
- cv2.INTER_CUBIC: This is slow but more efficient.
- cv2.INTER_LINEAR: This is primarily used when zooming is required. This is the default interpolation technique in OpenCV.

https://www.geeksforgeeks.org/image-resizing-using-opencv-python/
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./Media/Man_United.jpeg')

if img is not None:
    interpolation_area = cv2.resize(img,
                               (480, 480),
                               interpolation = cv2.INTER_AREA)
    
    interpolation_nearest = cv2.resize(img,
                               (480, 480),
                               interpolation=cv2.INTER_NEAREST)
    
    bigger = cv2.resize(img,
                        (2048, 2048))
    titles = ['Original', 'INTER_AREA', "INTER_NEAREST", "bigger"]
    images = [img, interpolation_area, interpolation_nearest, bigger]
    count = 4

    for i in range(count):
        plt.subplot(2, 2, i+1)
        plt.title(titles[i])
        plt.imshow(images[i])
    plt.show()
else:
    print("Check the file path again.")