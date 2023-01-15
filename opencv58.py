import cv2
import numpy as np
import matplotlib.pyplot as plt


# imgpath = "./standard_test_images/cameraman.tif"
# img = cv2.imread(imgpath, 0)

imgpath = "./standard_test_images/mandril_color.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


k = np.ones((5, 5), np.uint8)
# k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# k = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
print(k)


erosion = cv2.erode(img, k, iterations = 3)

dilation = cv2.dilate(img, k, iterations = 1)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)


outputs = [img, erosion, dilation, gradient]
titles = ['Original', 'erosion', 'Dilation', 'Gradient']

for i in range(len(outputs)):
    plt.subplot(2, 2, i+1)
    # plt.imshow(outputs[i], cmap="gray")
    plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()