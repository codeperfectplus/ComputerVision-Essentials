import cv2

img1 = cv2.imread('../Media/sample.jpeg')
img2 = cv2.imread('../Media/opencv-logo-white.png')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow("final image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()