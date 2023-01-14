import cv2
import matplotlib.pyplot as plt

imgpath1 = "./misc/4.1.01.tiff"
imgpath2 = "./misc/4.1.02.tiff"
img1 = cv2.imread(imgpath1, 1)
img2 = cv2.imread(imgpath2, 1)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.imshow(img1)
plt.title("Girl")
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(img2)
plt.title("Girl and Boy")
plt.xticks([])
plt.yticks([])

plt.show()

