import cv2
import matplotlib.pyplot as plt

imgpath1 = "./misc/4.1.01.tiff"
imgpath2 = "./misc/4.1.02.tiff"
img1 = cv2.imread(imgpath1, 1)
img2 = cv2.imread(imgpath2, 1)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

add = img1 + img2
sub1 = img1 - img2
sub2 = img2 - img1
# mul = img1 * 10
mul = img1 * img2
div = img1 / img2

titles = ['Girl', 'Boy and Girl', 'Addition', 'img1 - img2', 'img2 - img1', 'multiply', 'divide']
images = [img1, img2, add, sub1, sub2, mul, div]

for i in range(7):
    plt.subplot(1, 7, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

