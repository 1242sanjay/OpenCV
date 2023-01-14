import cv2
import matplotlib.pyplot as plt

imgpath = "./misc/4.1.01.tiff"
img = cv2.imread(imgpath, 0)

plt.imshow(img, cmap="gray")
plt.title("Gray colormap")
plt.xticks([])
plt.yticks([])
plt.show()

plt.imshow(img)
plt.title("Default colormap")
plt.xticks([])
plt.yticks([])
plt.show()

# cv2.imshow('girl', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
