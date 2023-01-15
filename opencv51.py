import cv2
import numpy as np
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/peppers_gray.tif"
img = cv2.imread(imgpath, 0)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title('Image')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
plt.hist(img.ravel(), 25, [0, 255])
plt.title('Histogram')

plt.show()



