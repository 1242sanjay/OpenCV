import cv2
import numpy as np
import matplotlib.pyplot as plt

# Histogram equalization
imgpath = "./standard_test_images/lena_color_512.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(img)

equalizeHist_r = cv2.equalizeHist(r)
equalizeHist_g = cv2.equalizeHist(g)
equalizeHist_b = cv2.equalizeHist(b)
equalizeHist = cv2.merge((equalizeHist_r, equalizeHist_g, equalizeHist_b))

# clahe = cv2.createCLAHE()
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_r = clahe.apply(r)
clahe_g = clahe.apply(g)
clahe_b = clahe.apply(b)
clahe = cv2.merge((clahe_r, clahe_g, clahe_b))



outputs = [img, equalizeHist, clahe]
titles = ['Original', 'equalizeHist', 'clahe']

for i in range(len(outputs)):
    plt.subplot(1, 3, i+1)
    plt.imshow(outputs[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()



