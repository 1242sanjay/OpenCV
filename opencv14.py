import cv2
import matplotlib.pyplot as plt

imgpath = "./misc/4.1.01.tiff"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.title("Color image with default colormap")
plt.xticks([])
plt.yticks([])
plt.show()

