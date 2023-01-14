import cv2
import matplotlib.pyplot as plt


imgpath = "./misc/4.1.01.tiff"

img = cv2.imread(imgpath, 1)

color_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
color_negative = abs(255-color_image)
gray_negative = abs(255-gray_image)

titles = ['Color image', 'GrayScale image', 'Color-Negative', 'GrayScale-Negative']
images = [color_image, gray_image, color_negative, gray_negative]
cmaps = [None, 'gray', None, 'gray']

for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap=cmaps[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()


