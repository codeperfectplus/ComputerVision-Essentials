''' Saving videos from Camera '''
import cv2

cap = cv2.VideoCapture(0)

#define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("./Media/output.avi", fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame,0)

        # write the filpped frame
        out.write(frame)

        cv2.imshow('video',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release video capture
cap.release()
out.release()
cv2.destroyAllWindows()
