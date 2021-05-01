'''
Edge detection with canny algo
edges = cv2.Canny('/path/to/img', minVal, maxVal, apertureSize, L2gradient)  

minVal= minimu, intensity gradent
L2gradient: Its default value is false, if value is true, Canny () uses a more computationally expensive equation to detect edges, 
which provides more accuracy at the cost of resources.
'''
import cv2

img = cv2.imread(r'./Media/face-001.jpg')
edges = cv2.Canny(img, 100, 100)
print(edges)

cv2.imshow("Edge Detected Image",edges)

k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("./Media/edge-detection.jpg", edges)
    cv2.destroyAllWindows()