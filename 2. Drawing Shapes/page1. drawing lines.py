import numpy as np
import cv2

# # create new blank image
# img = np.zeros((400, 400, 3))
img = cv2.imread('./messi5.jpg')

# draw a lines
cv2.line(img, (10, 10), (100, 10), (0, 255, 255), 1)
cv2.line(img, (10, 30), (100, 30), (255, 0, 255), 5)
cv2.line(img, (10, 60), (100, 60), (0, 255, 0), 10)

cv2.imshow('blank', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
