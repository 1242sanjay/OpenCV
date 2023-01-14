import cv2


imgpath = "./misc/4.1.01.tiff"
img = cv2.imread(imgpath, 1)

########################### scaling up - zoom ################################
# output = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
# output = cv2.resize(img, None, fx=1.5, fy=1, interpolation=cv2.INTER_LINEAR)
# output = cv2.resize(img, None, fx=1.5, fy=1, interpolation=cv2.INTER_CUBIC)
# output = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# output = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
# output = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
# output = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LANCZOS4)

########################## scaling down - shrinking ##############################
output = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)


cv2.imshow('Output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

