import cv2
import numpy as np

img = cv2.imread('./messi5.jpg')

# get original size
(h, w, ch) = img.shape

# center = (0, 0)
center = (w // 2, h // 2)

# create the translation matrix
t = np.float32([[1, 0, 100], [0, 1, 100]])

# apply the transformation
img_rotated = cv2.warpAffine(img, t, (w, h))

cv2.imshow('original', img)
cv2.imshow('rotated', img_rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()