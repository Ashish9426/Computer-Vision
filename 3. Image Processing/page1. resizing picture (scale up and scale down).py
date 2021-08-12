# importing package
import cv2
import numpy as np

img = cv2.imread('./messi5.jpg')
(h, w, ch) = img.shape
print(f"h: {h}, w: {w}, ch: {ch}")

img_scaled_up = cv2.resize(img, (w * 2, h * 2))
img_scaled_down = cv2.resize(img, (100, 100))

cv2.imshow("messi", img)
cv2.imshow("up", img_scaled_up)
cv2.imshow("down", img_scaled_down)

# wait for user to press any key
cv2.waitKey(0)
cv2.destroyAllWindows()
