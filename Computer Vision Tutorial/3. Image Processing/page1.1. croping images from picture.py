# importing package
import cv2
import numpy as np

img = cv2.imread('./messi5.jpg')

# extract face
face = img[50:155, 200:271]

# extract ball
ball = img[280:330, 330:390].copy()

# copy ball
# img[290:335, 50:110] = ball

cv2.imshow('messi', img)
cv2.imshow('face', face)
cv2.imshow('ball', ball)


# wait for user to press any key
cv2.waitKey(0)
cv2.destroyAllWindows()
