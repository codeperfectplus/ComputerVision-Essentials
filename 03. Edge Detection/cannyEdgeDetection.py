'''
Edge detection with canny algo
edges = cv2.Canny('/path/to/img', threshold1, threshold2, apertureSize, L2gradient)

L2gradient: Its default value is false, if value is true, Canny () uses a more computationally expensive equation to detect edges,
which provides more accuracy at the cost of resources.
'''
import cv2

img = cv2.imread(r'./Media/face-001.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# applying canny edge transformations
edges = cv2.Canny(gray_img, threshold1=30, threshold2=100)

# showing the output frame
cv2.imshow("Edge Detected Image", edges)

k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("./Media/edge-detection.jpg", edges)
    cv2.destroyAllWindows()
