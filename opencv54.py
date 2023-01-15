import cv2
import numpy as np
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/peppers_color.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

red_hist = cv2.calcHist([img], [0], None, [256], [0, 255])
green_hist = cv2.calcHist([img], [1], None, [256], [0, 255])
blue_hist = cv2.calcHist([img], [2], None, [256], [0, 255])

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title('Image')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.plot(red_hist, color='r')
plt.title('Histogram-Red')

plt.subplot(2, 2, 3)
plt.plot(green_hist, color='g')
plt.title('Histogram-Green')

plt.subplot(2, 2, 4)
plt.plot(blue_hist, color='b')
plt.title('Histogram-Blue')

plt.show()



