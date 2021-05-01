""" Drawing function in Opencv """

import  cv2

img = cv2.imread("./Media/apple.jpeg")
if img is not None:
    """ It will be create a line from (10, 10) to (100, 100)"""
    img = cv2.line(img,
                   pt1=(10, 10),
                   pt2=(100, 100),
                   color=(255, 255, 255),
                   thickness=2)
    
    cv2.imshow("output", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# other fucntions
cv2.arrowedLine()
cv2.rectangle()
'''