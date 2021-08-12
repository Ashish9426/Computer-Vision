import cv2
import numpy as np

# original colorful image
img = cv2.imread('./messi5.jpg')
print(img.shape)

# grayscale image
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(grayscale.shape)

cv2.imshow('messi-color', img)
cv2.imshow('messi-grayscale', grayscale)

cv2.waitKey(0)
cv2.destroyAllWindows()
