import cv2

windowName = "OpenCV video player"
cv2.namedWindow(windowName)
filename = "C:/Games/Desktop/pythonoutput/output.avi"
cap = cv2.VideoCapture(filename)


while cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow(windowName, frame)
    if ret:
        if cv2.waitKey(33) == 27:
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()