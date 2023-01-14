import cv2
import matplotlib.pyplot as plt


imgpath1 = "./misc/4.1.01.tiff"
imgpath2 = "./misc/4.1.02.tiff"
img1 = cv2.imread(imgpath1, 1)
img2 = cv2.imread(imgpath2, 1)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img1_not = cv2.bitwise_not(img1)
img_and = cv2.bitwise_and(img1, img2)
img_or = cv2.bitwise_or(img1, img2)
img_xor = cv2.bitwise_xor(img1, img2)

titles = ['img1', 'img2', 'bitwise not img1', 'bitwise and', 'bitwise or', 'bitwise xor']
images = [img1, img2, img1_not, img_and, img_or, img_xor]


for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()


