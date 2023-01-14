import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 99), (99, 0), (255, 0, 0), 2)
cv2.rectangle(img, (100, 120), (200, 170), (0, 255, 0), 5)
cv2.circle(img, (280, 280), 50, (0, 0, 255), -1)
cv2.ellipse(img, (200, 60), (100, 40), 0, 0, 360, (127, 127, 127), -1)

points = np.array([[80, 2], [125, 0], [170, 10], [230, 5], [30, 50]], np.int32)
points = points.reshape(-1, 1, 2)
cv2.polylines(img, [points], True, [0, 255, 255])

text = "Sanjay Kumar"
cv2.putText(img, text, (30, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0))


cv2.imshow('girl', img)
cv2.waitKey(0)
cv2.destroyAllWindows('girl')
