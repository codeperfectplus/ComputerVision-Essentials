"""
Template Matching is a method for searching and finding the location of a template image in a larger image.
OpenCV comes with a function cv2.matchTemplate() for this purpose. It simply slides the template image over the input
image (as in 2D convolution) and compares the template and patch of input image under the template image.
"""
import cv2
import numpy as np

source_color = cv2.imread(r"./Media/pieboard-templatematching.jpg")
#keeping source_color in colored to show the cordinate in original picture instead to grayscale
source_gray = cv2.cvtColor(source_color, cv2.COLOR_BGR2GRAY)
template_image = cv2.imread(r"./Media/port-templatematching.jpg", 0)
w,h = template_image.shape[::-1]

res = cv2.matchTemplate(source_gray, template_image, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

print(*loc)
for port in zip(*loc[::-1]):
    cv2.rectangle(source_color, port,(port[0] + w, port[1] + h), (0, 255, 255), 2)

cv2.imshow("Port Detected", source_color)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite('./Media/port-detected.jpeg', source_color)
    cv2.destroyAllWindows()
