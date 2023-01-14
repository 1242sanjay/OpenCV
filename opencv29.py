import cv2
import matplotlib.pyplot as plt


imgpath1 = "./misc/4.1.01.tiff"
imgpath2 = "./misc/4.1.02.tiff"
img1 = cv2.imread(imgpath1, 1)
img2 = cv2.imread(imgpath2, 1)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

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


