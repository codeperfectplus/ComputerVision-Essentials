""" Face detection using haarcascade_frontalface and eye classifier """

import cv2

# Path
face_cascade = cv2.CascadeClassifier('./assets/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./assets/haarcascade_eye.xml')


def detectedFace(img):
    img = cv2.imread(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.4, 5)

    for face in faces:
        x, y, width, height = face
        # draw a rectangle for detection
        cv2.rectangle(
                img,
                (x, y),
                (x + width, y + height),
                (0, 0, 255),
                1,
        )
        roi_gray = gray[y:y+height, x:x+width]
        roi_color = img[y:y+height, x:x+width]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                    roi_color,
                    (ex, ey),
                    (ex+ew, ey+eh),
                    (0, 255, 0),
                    2,
            )

    cv2.imshow('Face Detection', img)
    k = cv2.waitKey(0) & 0xFF

    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('./Media/face-detected.jpeg', img)
        cv2.destroyAllWindows()


path_img = './Media/face-001.jpg'
detectedFace(path_img)
