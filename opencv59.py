import cv2
import numpy as np
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/peppers_color.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
original_img = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)
print(hierarchy)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

outputs = [original_img, gray, thresh, img]
titles = ['Original', 'Gray', 'Thresh', 'Contours']

for i in range(len(outputs)):
    plt.subplot(2, 2, i+1)
    if titles[i] == 'Gray':
        plt.imshow(outputs[i], cmap="gray")
    else:
        plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()