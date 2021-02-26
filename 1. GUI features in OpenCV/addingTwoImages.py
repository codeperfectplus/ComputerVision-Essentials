""" Adding two images in opencv """

import cv2

alpha = 0.5
beta = 1 - alpha

src1 = cv2.imread('./Media/sample.jpeg')
src2 = cv2.imread('./Media/sample2.jpeg')

# Check for image loading or not
if src1 is None:
    print("Error loading Src1")
    exit(-1)
elif src2 is None:
    print("Error loading src2")
    exit(-1)

# cretae addWeighted method
dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
cv2.imshow('Mixed Image', dst)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()