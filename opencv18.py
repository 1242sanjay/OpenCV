import cv2

windowName = "Live video feed"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)

#######################################################
for i in range(50):
    print(cap.get(i))   # exactly don't know how many values are there
#######################################################

# Resolution
print("Width : ", cap.get(3))
print("Height : ", cap.get(4))

cap.set(3, 640)
cap.set(4, 360)

print("Width : ", cap.get(3))
print("Height : ", cap.get(4))

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:
    ret, frame = cap.read()
    output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow(windowName, frame)       # for color video
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()