""" Image segmentation using K-Menas """

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('./Media/nature.png')

# reshape the image to a 2D array of pixels and 3 array values
pixels_values = image.reshape((-1, 3))

# conerting to float32
pixels_values = np.float32(pixels_values)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# Number of clusters]
K = 3

_, labels, (centers) = cv2.kmeans(pixels_values,
                                  K=K,
                                  bestLabels=None,
                                  criteria=criteria,
                                  attempts=10,
                                  flags=cv2.KMEANS_RANDOM_CENTERS)

# converting to 8 bit values
centers = np.uint8(centers)

# flatten the labels array
labels = labels.flatten()

# convert all pixels to the color of the centroids
segmented_image = centers[labels]

segmented_image = segmented_image.reshape(image.shape)

# show the original and segmented output
cv2.imshow('Original', image)
cv2.imshow('Segmented', segmented_image)

# saving the output
cv2.imwrite('./Media/nature_output.png', segmented_image)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
