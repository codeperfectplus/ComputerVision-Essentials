import cv2
from skimage import io

# reading the image
img = cv2.imread('./Media/sample.jpeg')

# changing image from BGR to RGB for correct output
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# showing output
io.imshow(img)
io.show()
