from matplotlib import pyplot as plt
import cv2

img = cv2.imread('../Media/sample.jpeg', 0)
plt.imshow(img, cmap="gray")
plt.show()