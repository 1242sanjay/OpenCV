import cv2
import numpy as np
import matplotlib.pyplot as plt

w = 800
h = 600
windowName = "Live video Max RGB filter"
cap = cv2.VideoCapture(0)
cap.set(3, w)
cap.set(4, h)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False


while ret:
    ret, frame = cap.read()
    b, g, r = cv2.split(frame)
    m = np.maximum(np.maximum(r, g), b)
    r[r < m] = 0
    g[g < m] = 0
    b[b < m] = 0

    output = cv2.merge((b, g, r))

    cv2.imshow(windowName, output)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyWindow(windowName)
cap.release()









