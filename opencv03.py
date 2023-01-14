import cv2

imgpath = "./misc/4.1.01.tiff"
img = cv2.imread(imgpath)

cv2.namedWindow('girl', cv2.WINDOW_AUTOSIZE)
cv2.imshow('girl', img)
cv2.waitKey(0)
cv2.destroyWindow('girl')
