import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


# Image restoration by Inpainting
imgpath = "./standard_test_images/damage.tif"
maskpath = "./standard_test_images/mask.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mask = cv2.imread(maskpath, 0)


output1 = cv2.inpaint(img, mask, 5, cv2.INPAINT_TELEA)
output2 = cv2.inpaint(img, mask, 5, cv2.INPAINT_NS)

titles = ['Original Image', 'Mask', 'TELEA', 'NS']
outputs = [img, mask, output1, output2]

for i in range(len(outputs)):
    plt.subplot(2, 2, i+1)
    if i == 1:
        plt.imshow(outputs[i], cmap='gray')
    else:
        plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()



