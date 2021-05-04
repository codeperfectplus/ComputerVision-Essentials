''' Showing output using matplotlib '''

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./Media/sample.jpeg', 0)

plt.imshow(img, cmap="gray")
plt.title('Sample Image')
plt.xticks([])
plt.yticks([])
plt.show()
