import cv2

imgpath = "./misc/4.1.01.tiff"

# Default mode
# img = cv2.imread(imgpath, 1)

# Greyscale image mode
# img = cv2.imread(imgpath, 0)

# Also save alpha transparency channel in the image
img = cv2.imread(imgpath, -1)


cv2.imshow('girl', img)
cv2.waitKey(0)
cv2.destroyAllWindows('girl')
