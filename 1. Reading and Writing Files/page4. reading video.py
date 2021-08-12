import numpy as np
import cv2

# capture the default camera
capture = cv2.VideoCapture(0)
ret, frame = capture.read()
cv2.imshow('output', frame)

while capture.isOpened():
    # read a frame
    ret, frame = capture.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('output', frame)
    cv2.imshow('output-gray', grayscale)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
