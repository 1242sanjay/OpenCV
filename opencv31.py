import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "./misc/4.1.01.tiff"
img = cv2.imread(imgpath, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

########################### Geometric operation(shifting image) ################################

# rows, columns, channels = img.shape
# T = np.float32([[1, 0, 50], [0, 1, -50]])
# print(T)
# output = cv2.warpAffine(img, T, (columns, rows))
#
# plt.imshow(output)
# plt.title("Shifted image")
# plt.show()

################################## Rotation #############################################

rows, columns, channels = img.shape
R = cv2.getRotationMatrix2D((columns/2, rows/2), 45, 1)
print(R)
output = cv2.warpAffine(img, R, (columns, rows))

plt.imshow(output)
plt.title('Rotated image')
plt.show()




plt.imshow(output)
plt.title("Shifted image")
plt.show()

