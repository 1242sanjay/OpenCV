import cv2
import numpy as np

windowName = "Preview"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)


while cap.isOpened():
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Blue Color
    low = np.array([100, 50, 50])
    high = np.array([140, 255, 255])

    # # Green Color
    # low = np.array([40, 50, 50])
    # high = np.array([80, 255, 255])

    # # Red Color
    # low = np.array([40, 50, 50])
    # high = np.array([80, 255, 255])

    image_mask = cv2.inRange(hsv, low, high)
    output = cv2.bitwise_and(frame, frame, mask = image_mask)

    cv2.imshow("Image mask", image_mask)
    cv2.imshow(windowName, frame)
    cv2.imshow("Color Tracking", output)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()