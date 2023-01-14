import cv2
import numpy as np
import time

windowName = "Live Video Feed"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

rows, columns, channels = frame.shape
angle = 0
scale = 0.1

while True:
    ret, frame = cap.read()
    if angle == 360:
        angle=0
    if scale <2:
        scale = scale + 0.01
    elif scale >= 2:
        scale = 0.1
    R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, scale)
    print(R)
    output = cv2.warpAffine(frame, R, (columns, rows))
    cv2.imshow(windowName, output)
    angle = angle + 1
    time.sleep(0.01)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyWindow(windowName)
