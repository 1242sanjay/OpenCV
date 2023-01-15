import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/house.tif"
img = cv2.imread(imgpath, 0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Canny edge detection
L1 = cv2.Canny(img, 50, 350, L2gradient=False)
L2 = cv2.Canny(img, 50, 350, L2gradient=True)



titles = ['Original Image', 'L1', 'L2']
outputs = [img, L1, L2]

for i in range(len(outputs)):
    plt.subplot(1, 3, i+1)
    plt.imshow(outputs[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()



