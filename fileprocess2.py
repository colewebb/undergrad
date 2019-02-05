import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('image.png', 0)
# greyscale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
binary = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
output = cv.connectedComponentsWithStats(binary, 8, cv.CV_32S)
img2 = binary
i = 2
while i < len(output[2]):
    if output[2][i][4] >= 100:
        img2[output[1] == i + 1] = 255
    else:
        print(output[2][i])
    i = i + 1
# print(len(output[1][12]))
# print(output[1][1])
# print(output[2])
# cv.imwrite(".\imagegrey.png", binary)

# ret, Ithresh = cv.threshold(greyscale, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
# comp = cv.connectedComponentsWithStats(greyscale)

plt.imshow(img2, 'gray')
plt.show()
