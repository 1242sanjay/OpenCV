import cv2
import numpy as np
import matplotlib.pyplot as plt


# Live video kmeans clustering - Quantization
windowName = "Live video Kmeans clustering"
cap = cv2.VideoCapture(0)
cap.set(3, 100)
cap.set(4, 100)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False


while ret:
    ret, frame = cap.read()

    z = frame.reshape((-1, 1))
    z = np.float32(z)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    k = 2
    ret, label, center = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    output = res.reshape((frame.shape))

    cv2.imshow(windowName, output)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyWindow(windowName)
cap.release()









