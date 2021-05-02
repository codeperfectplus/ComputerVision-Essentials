""" Adding two image using addWeighted() """
import cv2

img1 = cv2.imread('./Media/sample.jpeg')
img2 = cv2.imread('./Media/opencv-logo-white.png')

# resizing the image for arithmatic operations
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

output_img = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow("final image", output_img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()