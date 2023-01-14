import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "./standard_test_images/lake.tif"
img = cv2.imread(imgpath, 0)

block_size = 21
constant = 2

th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)


outputs = [img, th1, th2]
titles = ['Original', 'Mean Adaptive', 'Guassian Adaptive']

for i in range(len(outputs)):
    plt.subplot(1, 3, i+1)
    plt.imshow(outputs[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

