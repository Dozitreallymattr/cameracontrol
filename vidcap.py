import numpy as np
import cv2, time


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc=cv2.cv.CV_FOURCC(*'XVID')

today=time.time()
filena = "output" + str(today) + ".avi"
filename = "/home/pi/saves/" + filena

out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # write the frame out
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
