import cv2
import matplotlib.pyplot as plt


imgpath = "./misc/4.1.01.tiff"

img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

titles = ['Original Image', 'Red', 'Green', 'Blue']
cmaps = [None, 'Reds', 'Greens', 'Blues']
images = [cv2.merge((r, g, b)), r, g, b]

for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap=cmaps[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


