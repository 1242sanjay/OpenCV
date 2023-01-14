import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:
    ret, frame = cap.read()
    output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # cv2.imshow("Colored video", frame)       # for color video
    cv2.imshow("Black and white video", output)       # for black and white video
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()