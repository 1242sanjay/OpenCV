import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "./misc/4.1.01.tiff"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


rows, columns, channels = img.shape
point1 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
point2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
P = cv2.getPerspectiveTransform(point1, point2)
print(P)
output = cv2.warpPerspective(img, P, (columns, rows))

plt.imshow(output)
plt.title('Changed perspective')
plt.show()

