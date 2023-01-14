import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/peppers_color.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# identity
# k = np.array(([0, 0, 0], [0, 1, 0], [0, 0, 0]), np.float32)

# detect edge
# k = np.array(([1, 0, -1], [0, 0, 0], [-1, 0, 1]), np.float32)
# k = np.array(([0, 1, 0], [1, -4, 1], [0, 1, 0]), np.float32)
# k = np.array(([-1, -1, -1], [-1, 8, -1], [-1, -1, -1]))

# Box blurr
# k = np.array(np.ones((12, 12), np.float32)) / 144

# sharp
k = np.array(([0, -1, 0], [-1, 5, -1], [0, -1, 0]), np.float32)

print(k)
print(type(k))

output = cv2.filter2D(img, -1, k)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(output)
plt.title("Filtered Image")
plt.xticks([])
plt.yticks([])


plt.show()



