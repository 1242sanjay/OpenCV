import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "./misc/4.1.01.tiff"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


rows, columns, channels = img.shape
point1 = np.float32([[100, 100], [300, 100], [100, 300]])
point2 = np.float32([[200, 150], [400, 150], [200, 400]])
A = cv2.getAffineTransform(point1, point2)
print(A)
output = cv2.warpAffine(img, A, (columns, rows))

plt.imshow(output)
plt.title('Transformed image')
plt.show()

