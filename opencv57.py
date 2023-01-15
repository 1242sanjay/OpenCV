import cv2
import numpy as np
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/cameraman.tif"
img = cv2.imread(imgpath, 0)

th = 0
max_val = 255
ret, binary_inv = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

k = np.ones((5, 5), np.uint8)
# k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# k = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
print(k)


erosion = cv2.erode(binary_inv, k, iterations = 3)

dilation = cv2.dilate(binary_inv, k, iterations = 1)

gradient = cv2.morphologyEx(binary_inv, cv2.MORPH_GRADIENT, k)


outputs = [img, binary_inv, erosion, dilation, gradient]
titles = ['Original', 'Binary inversion', 'erosion', 'Dilation', 'Gradient']

for i in range(len(outputs)):
    plt.subplot(2, 3, i+1)
    plt.imshow(outputs[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()