import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/peppers_color.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

box = cv2.boxFilter(img, -1, (53, 53))
blur = cv2.blur(img, (25, 25))
guassian = cv2.GaussianBlur(img, (37, 37), 0)

titles = ['Original Image', 'Box filter', 'Blur filter', 'Guassian blur']
outputs = [img, box, blur, guassian]

for i in range(len(outputs)):
    plt.subplot(2, 2, i+1)
    plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()



