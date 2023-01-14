import cv2
import numpy as np
import time

imgpath = "./misc/4.1.01.tiff"
img = cv2.imread(imgpath, 1)


rows, columns, channels = img.shape

angle = 0
while True:
    if angle == 360:
        angle=0
    R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, 1)
    print(R)
    output = cv2.warpAffine(img, R, (columns, rows))
    cv2.imshow('Rotated Image', output)
    angle = angle + 1
    time.sleep(0.01)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyWindow("Rotated image")
