import cv2

img  = cv2.imread('./Media/Shapes.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(11,11),0) #The values need to be >1 and odd

# creating binary thresholding
ret, th = cv2.threshold(blur,220,255,cv2.THRESH_BINARY_INV) # Inverse Binary thresholding technique

# finding and drawing contour
(cnts,_) = cv2.findContours(th.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,cnts,-1,(0,0,0),2)

cv2.imshow('image',img)
cv2.imwrite("./Media/Shape_Detected.png",img) # Save the contoured image
cv2.waitKey(0)
cv2.destroyAllWindows()
