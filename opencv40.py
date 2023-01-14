import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/mandril_color.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rows, columns, channels = img.shape
p = 0.05

output = np.zeros(img.shape, np.uint8)
for i in range(rows):
    for j in range(columns):
        r = random.random()
        if r < p/2:
            #  pepper sprinkled
            output[i][j] = [0, 0, 0]
        elif r < p:
            # salt sprinkled
            output[i][j] = [255, 255, 255]
        else:
            output[i][j] = img[i][j]

plt.imshow(output)
plt.title("Image with salt and pepper noise")
plt.xticks([])
plt.yticks([])
plt.show()



