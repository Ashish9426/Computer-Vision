# importing package
import cv2
import numpy as np

img = cv2.imread('./messi5.jpg')

# separate the channels
(b, g, r) = cv2.split(img)

# merge the channels
img_red = cv2.merge([b, g, r + 100])
img_green = cv2.merge([b, g + 100, r])
img_blue = cv2.merge([b + 100, g, r])

cv2.imshow('messi', img)
cv2.imshow('messi-red', img_red)
cv2.imshow('messi-green', img_green)
cv2.imshow('messi-blue', img_blue)

# wait for user to press any key
cv2.waitKey(0)
cv2.destroyAllWindows()
