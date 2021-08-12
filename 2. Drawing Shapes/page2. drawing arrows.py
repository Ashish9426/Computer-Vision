import numpy as np
import cv2

# # create new blank image
# img = np.zeros((400, 400, 3))
img = cv2.imread('./messi5.jpg')

# draw a arrows
cv2.arrowedLine(img, (50, 50), (200, 50), (0, 255, 0), 5, 8, 0)
cv2.arrowedLine(img, (50, 100), (200, 100), (0, 255, 255), 1, 4, 0)
cv2.arrowedLine(img, (50, 200), (200, 200), (0, 0, 255), 10, 8, 0)


cv2.imshow('blank', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
