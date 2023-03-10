import cv2
import numpy as np


def emptyFunction():
    pass


def main():
    img = np.zeros((512, 512, 3), np.uint8)
    windowName = 'OpenCV BGR Color Palette'
    cv2.namedWindow(windowName)

    cv2.createTrackbar('Blue', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('Green', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('Red', windowName, 0, 255, emptyFunction)

    while True:
        cv2.imshow(windowName, img)
        if cv2.waitKey(1) == 27:
            break

        blue = cv2.getTrackbarPos('B', windowName)
        green = cv2.getTrackbarPos('G', windowName)
        red = cv2.getTrackbarPos('R', windowName)

        img[:] = [blue, green, red]

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()