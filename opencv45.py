import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/house.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Sobel operater
edgesx = cv2.Sobel(img, -1, dx=1, dy=0, ksize=11, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
edgesy = cv2.Sobel(img, -1, dx=0, dy=1, ksize=11, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

# Scharr operator
# edgesx = cv2.Scharr(img, -1, dx=1, dy=0, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
# edgesy = cv2.Scharr(img, -1, dx=0, dy=1, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

edges = edgesx + edgesy


titles = ['Original Image', 'Edges', 'Edgesx', 'Edgesy']
outputs = [img, edges, edgesx, edgesy]

for i in range(len(outputs)):
    plt.subplot(2, 2, i+1)
    plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()



