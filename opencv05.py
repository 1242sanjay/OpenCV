import cv2

imgpath = "./misc/4.1.01.tiff"
img = cv2.imread(imgpath, 0)

outpath = "C:/Users/HP/Desktop/output.jpg"


cv2.imshow('girl', img)
cv2.imwrite(outpath, img)
cv2.waitKey(0)
cv2.destroyAllWindows('girl')
