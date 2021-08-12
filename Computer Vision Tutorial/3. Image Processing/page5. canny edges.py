import cv2
import numpy as np


def function1():
    img = cv2.imread('./messi5.jpg')

    img_edges = cv2.Canny(img, 255, 255)

    cv2.imshow('original', img)
    cv2.imshow('edges detected', img_edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function1()


def function2():
    # capture the default camera
    capture = cv2.VideoCapture(1)
    ret, frame = capture.read()
    cv2.imshow('output', frame)

    while capture.isOpened():
        # read a frame
        ret, frame = capture.read()

        img_edges = cv2.Canny(frame, 255, 255)

        cv2.imshow('output', frame)
        cv2.imshow('output-edges', img_edges)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


function2()