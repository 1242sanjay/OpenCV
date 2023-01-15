import cv2
import numpy as np
import matplotlib.pyplot as plt


# Kmeans clustering on images Quantization
imgpath = "./standard_test_images/peppers_color.tif"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

z = img.reshape((-1, 1))
z = np.float32(z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 2
ret, label1, center1 = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
center1 = np.uint8(center1)
res1 = center1[label1.flatten()]
output1 = res1.reshape((img.shape))


k = 2
ret, label2, center2 = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
center2 = np.uint8(center2)
res2 = center2[label2.flatten()]
output2 = res2.reshape((img.shape))

k = 8
ret, label3, center3 = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
center3 = np.uint8(center3)
res3 = center3[label3.flatten()]
output3 = res3.reshape((img.shape))


titles = ['Original Image', 'k=2', 'k=4', 'k=8']
outputs = [img, output1, output2, output3]

for i in range(len(outputs)):
    plt.subplot(2, 2, i+1)
    plt.imshow(outputs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()



