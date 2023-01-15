import cv2
import numpy as np
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/peppers_gray.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(img)

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title('Image')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.hist(r.ravel(), 256, [0, 255])
plt.title('Histogram-Red')

plt.subplot(2, 2, 3)
plt.hist(g.ravel(), 256, [0, 255])
plt.title('Histogram-Green')

plt.subplot(2, 2, 4)
plt.hist(b.ravel(), 256, [0, 255])
plt.title('Histogram-Blue')

plt.show()



