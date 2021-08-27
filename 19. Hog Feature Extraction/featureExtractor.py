''' Feature extraction using hog and skimage '''

from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from matplotlib import pyplot as plt

img = imread("./Media/coins.jpg")

# applying the hog algorithm
fd, hog_image = hog(img,
                    orientations=9,
                    pixels_per_cell=(8, 8),
                    cells_per_block=(2,2),
                    visualize=True,
                    multichannel=True)

plt.axis("off")
plt.imshow(hog_image, cmap='gray')
plt.savefig("./Media/coins_hog.png")
plt.show()
