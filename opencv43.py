import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


imgpath = "./standard_test_images/peppers_color.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rows, columns, channels = img.shape
p = 0.2

noisy = np.zeros(img.shape, np.uint8)
for i in range(rows):
    for j in range(columns):
        r = random.random()
        if r < p/2:
            #  pepper sprinkled
            noisy[i][j] = [0, 0, 0]
        elif r < p:
            # salt sprinkled
            noisy[i][j] = [255, 255, 255]
        else:
            noisy[i][j] = img[i][j]

denoised = cv2.medianBlur(noisy, 3)

outputs = [img, noisy, denoised]
titles = ['Original', 'Noisy', 'Denoised']

for i in range(len(outputs)):
    plt.subplot(1, 3, i+1)
    plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()



