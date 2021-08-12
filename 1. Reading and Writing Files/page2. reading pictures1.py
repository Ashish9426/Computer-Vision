# importing package
import cv2
import numpy as np

# step 1: open the file
img = cv2.imread('./messi5.jpg')

# step 2: perform operation(s)

# step 2.1: take an action
# step 2.2: generate output
# step 2.3: save the changes to a new file
# step 2.4: show the file on screen
cv2.imshow('messi', img)

# wait for user to press any key
cv2.waitKey(0)
cv2.destroyAllWindows()

# step 3: close the file
