import cv2

imgpath = "./misc/4.1.01.tiff"
img = cv2.imread(imgpath, 0)

print(img)
print(type(img))
print(img.dtype)
print(img.shape)
print(img.ndim)
print(img.size)

cv2.imshow('girl', img)
cv2.waitKey(0)
cv2.destroyAllWindows('girl')
