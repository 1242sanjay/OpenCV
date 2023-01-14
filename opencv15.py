import cv2
import matplotlib.pyplot as plt

j = 0
for filename in dir(cv2):
    if filename.startswith("COLOR_"):
        print(filename)
        j = j + 1
print('There are {} color conversion flag in OpenCV'.format(j+1))
