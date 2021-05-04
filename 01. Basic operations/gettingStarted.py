''' Getting started with opencv

Reading and saving image with opencv using waitKey
'''
import cv2

#load an color image in grayscale color
img = cv2.imread('./Media/sample.jpeg',0)

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

# esc key to exit
if k == 27:
    cv2.destroyAllWindows()

# s key to save and exit
elif k == ord('s'):
    cv2.imwrite("./Media/sample2.jpeg", img)
    cv2.destroyAllWindows()
