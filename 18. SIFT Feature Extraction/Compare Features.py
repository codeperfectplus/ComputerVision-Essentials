import numpy as np
import cv2

# loading and resizing the image 
img1 = cv2.imread('./Media/book.png')
img2 = cv2.imread('./Media/book_on_table.jpeg')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

keypoints1, descrptors1 = sift.detectAndCompute(img1, None)
keypoints2, descrptors2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descrptors1, descrptors2)
matches = sorted(matches, key= lambda x: x.distance)

matched_img = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:20], img2, flags=2)

# showing the output
cv2.imshow('image', cv2.resize(matched_img, (800, 600)))

k = cv2.waitKey(0) & 0xff

if k == 27:
    cv2.destroyAllWindows()
