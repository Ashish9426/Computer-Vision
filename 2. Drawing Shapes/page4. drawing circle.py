import numpy as np
import cv2

# # create new blank image
# img = np.zeros((400, 400, 3))
img = cv2.imread('./messi5.jpg')

# draw a cirles
cv2.circle(img, (50, 50), 20, (255, 0, 0), 3)
cv2.circle(img, (100, 100), 30, (0, 255, 0), -1)
cv2.circle(img, (200, 200), 40, (0, 0, 255), -1)
cv2.circle(img, (300, 200), 40, (255, 0, 255), 2)

cv2.imshow('blank', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
