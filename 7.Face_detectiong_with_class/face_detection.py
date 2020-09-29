import cv2


# Global variable
route = '/usr/share/opencv4/haarcascades/'
face_path = route + 'haarcascade_frontalface_default.xml'
eye_path = route + 'haarcascade_eye.xml'
path_img = 'Media/face-001.jpg'

face_cascade = cv2.CascadeClassifier(face_path)
eye_cascade = cv2.CascadeClassifier(eye_path)

font = cv2.FONT_HERSHEY_SIMPLEX


# Class main
class faceDetecting:
    def faceDetected(self):

        img = cv2.imread(path_img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for face in faces:
            x, y, width, height = face
            # draw a rectangle for detection
            cv2.rectangle(
                    img,
                    (x, y),
                    (x + width, y + height),
                    (187, 148, 178),
                    3,
            )
            roi_gray = gray[y:y+height, x:x+width]
            roi_color = img[y:y+height, x:x+width]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(
                        roi_color,
                        (ex, ey),
                        (ex + ew, ey + eh),
                        (0, 255, 0),
                        2,
                )

                cv2.putText(
                        img,
                        'hi human',
                        (x, y + height + 40),
                        font,
                        0.7,
                        (192, 207, 18),
                        2,
                        )

                cv2.imshow('Face Detection', img)
                k = cv2.waitKey(0) & 0xFF

                if k == 27:
                    cv2.destroyAllWindows()
                elif k == ord('s'):
                    cv2.imwrite('Media/face-detected.jpeg', img)
                    cv2.destroyAllWindows()


# Main
def main(args):
    feis = faceDetecting()
    feis.faceDetected()
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
