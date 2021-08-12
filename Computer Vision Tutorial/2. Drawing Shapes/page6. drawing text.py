import numpy as np
import cv2

# # create new blank image
# img = np.zeros((400, 400, 3))
img = cv2.imread('./messi5.jpg')

# draw a texts
cv2.putText(img, 'OpenCV', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_4)

cv2.putText(img, 'OpenCV', (10, 70), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 255, 255), 2, cv2.LINE_8)

cv2.putText(img, 'OpenCV', (10, 110),cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.9, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('blank', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
