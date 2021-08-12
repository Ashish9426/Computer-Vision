import numpy as np
import cv2

# # create new blank image
# img = np.zeros((400, 400, 3))
img = cv2.imread('./messi5.jpg')

# draw a rectangle
cv2.rectangle(img, (20, 20), (150, 150), (0, 0, 255), cv2.LINE_4)
cv2.rectangle(img, (40, 40), (170, 170), (0, 255, 255), cv2.LINE_4)

cv2.imshow('blank', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
