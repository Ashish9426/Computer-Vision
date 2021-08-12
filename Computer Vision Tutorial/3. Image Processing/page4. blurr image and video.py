import cv2
import numpy as np


def blurr1():
    img = cv2.imread('./messi5.jpg')

    # blurr matrix
    kernel = np.ones((10, 10), dtype=np.float32) / 100

    # blurr the image
    img_blurred = cv2.filter2D(img, -1, kernel)

    cv2.imshow('original', img)
    cv2.imshow('blurred', img_blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# blurr1()


def blurr2():
    img = cv2.imread('./messi5.jpg')

    # blurr the image
    # img_blurred = cv2.blur(img, (10, 10))
    img_blurred = cv2.GaussianBlur(img, (9, 9), 0)

    cv2.imshow('original', img)
    cv2.imshow('blurred', img_blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# blurr2()


def blurr_face():
    img = cv2.imread('./messi5.jpg')

    # crop the face
    face = img[50:155, 200:271].copy()

    # blurr the face
    face_blurred = cv2.blur(face, (10, 10))

    # put the blurred face back in the original image
    img_with_blurred_face = img.copy()
    img_with_blurred_face[50:155, 200:271] = face_blurred

    cv2.imshow('original', img)
    cv2.imshow('blurred_face', img_with_blurred_face)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# blurr_face()


def blurr_video():
    # capture the default camera
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    cv2.imshow('output', frame)

    while capture.isOpened():
        # read a frame
        ret, frame = capture.read()

        face = frame[50:155, 200:271].copy()
        face_blurred = cv2.blur(face, (10, 10))

        frame_with_blurred_face = frame.copy()
        frame_with_blurred_face[50:155, 200:271] = face_blurred

        cv2.imshow('output', frame)
        cv2.imshow('output-blurred', frame_with_blurred_face)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


blurr_video()