import cv2
import numpy as np
import matplotlib.pyplot as plt

# Histogram equalization
imgpath = "./standard_test_images/lena_color_512.tif"
img = cv2.imread(imgpath, 0)


equalizeHist = cv2.equalizeHist(img)

# clahe = cv2.createCLAHE()
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe = clahe.apply(img)


outputs = [img, equalizeHist, clahe]
titles = ['Original', 'equalizeHist', 'clahe']

for i in range(len(outputs)):
    plt.subplot(1, 3, i+1)
    plt.imshow(outputs[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()



