""" Drawing function in Opencv """

import cv2

img = cv2.imread("./Media/apple.jpeg")
if img is not None:
    """ It will be create a line from (10, 10) to (100, 100)"""
    img = cv2.line(img,
                   pt1=(10, 10),
                   pt2=(180, 100),
                   color=(255, 255, 255),
                   thickness=2)

    img = cv2.arrowedLine(img,
                          pt1=(20, 20),
                          pt2=(300, 300),
                          color=(0, 255, 255),
                          thickness=2)
    
    img = cv2.rectangle(img, 
                        pt1=(250, 0),
                        pt2=(450, 250),
                        color=(0, 255, 0),
                        thickness=2)

    img = cv2.circle(img,
                     center=(100, 100), 
                     radius=50, 
                     color=(255, 0, 255), 
                     thickness=-1)

    cv2.imshow("output", img)
else:
    print('file not found.')
    
cv2.waitKey(0)
cv2.destroyAllWindows()
