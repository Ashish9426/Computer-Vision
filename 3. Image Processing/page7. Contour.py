import cv2
import numpy as np


def function1():
    img = cv2.imread('./shapes.jpg')

    # get the binary image
    img_binary = cv2.Canny(img, 255, 255)

    # find the contours
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # get all the contour
    # print(contours)

    for contour in contours:
        print(contour)

    cv2.imshow('original', img)
    cv2.imshow('binary', img_binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function1()


def function2():
    # img = cv2.imread('./myimage.png')
    img = cv2.imread('./shapes.jpg')

    # get the binary image
    img_binary = cv2.Canny(img, 255, 255)

    # find the contours
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # draw contours
    for contour in contours:
        cv2.drawContours(img, [contour], -1, (0, 0, 255), 2)

    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

    cv2.imshow('original', img)
    # cv2.imshow('binary', img_binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function2()


def function3():
    img = cv2.imread('./myimage.png')

    # get the binary image
    img_binary = cv2.Canny(img, 255, 255)

    # find the contours
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # draw contours
    index = 1
    for contour in contours:
        # find the bounding rect
        (x, y, w, h) = cv2.boundingRect(contour)

        # draw the bounding rectangle for every contour
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # crop the contour
        img_contour = img[y: y + h, x: x + w]
        # cv2.imshow(f'shape_{index}', img_contour)

        # save all the extracted images to the shapes directory
        cv2.imwrite(f'shapes/shape_{index}.png', img_contour)

        index += 1

    cv2.imshow('original', img)
    # cv2.imshow('binary', img_binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function3()


def function4():
    img = cv2.imread('./shapes.jpg')

    # get the binary image
    img_binary = cv2.Canny(img, 255, 255)

    # find the contours
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # draw contours
    for contour in contours:
        # find the bounding rect
        (x, y, w, h) = cv2.boundingRect(contour)

        # approximate shape of the detected contour
        arc_length = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01 * arc_length, True)

        # print(f"edges = {len(approx)}")
        edges = len(approx)

        shape = ''
        if edges == 3:
            shape = 'triangle'
        elif edges == 4:
            shape = 'rectangle'
        elif edges == 5:
            shape = 'pentagon'
        elif edges == 6:
            shape = 'hexagon'
        elif edges > 10:
            shape = 'circle'

        # print(f"shape = {shape}")

        # find the contour moment
        moment = cv2.moments(contour)

        # center of the contour
        cx = int(moment['m10'] / moment['m00'])
        cy = int(moment['m01'] / moment['m00'])

        cv2.putText(img, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow('original', img)
    # # cv2.imshow('binary', img_binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# function4()