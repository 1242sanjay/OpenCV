import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/house.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

edges = cv2.Laplacian(img, -1, ksize=11, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)


titles = ['Original Image', 'Edges']
outputs = [img, edges]

for i in range(len(outputs)):
    plt.subplot(1, 2, i+1)
    plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()



