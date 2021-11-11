import cv2
import numpy as np
from numpy.core.fromnumeric import shape
from scipy import ndimage
import math

pi = 3.14159265359
img = np.zeros(shape=(500, 500, 3))
cv2.putText(img, "1", (50, 50), cv2.FONT_HERSHEY_PLAIN,
            1, (0, 255, 0), 2)
cv2.putText(img, "2", (250, 250), cv2.FONT_HERSHEY_PLAIN,
            1, (0, 255, 0), 2)
cv2.putText(img, "3", (450, 450), cv2.FONT_HERSHEY_PLAIN,
            1, (0, 255, 0), 2)
cv2.imshow("img", img)
angle = 15
rotated = ndimage.rotate(img, angle, axes=(1, 0))
cv2.imshow("rot", rotated)
cv2.waitKey(0)
