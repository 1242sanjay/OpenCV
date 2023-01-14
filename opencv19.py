import cv2

windowName = "Live webcam video feed capture"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)

filename = "C:/Games/Desktop/pythonoutput/output.avi"
codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
framerate = 30
resolution = (640, 480)
videoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    videoFileOutput.write(frame)

    cv2.imshow(windowName, frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
videoFileOutput.release()
cap.release()