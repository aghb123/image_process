# 边缘检测
import cv2.Error
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../image/horse.jpg", 0)

# Sobel算子
x = cv.Sobel(img, cv.CV_16S, 1, 0)
y = cv.Sobel(img, cv.CV_16S, 0, 1)

absx = cv.convertScaleAbs(x)
absy = cv.convertScaleAbs(y)

# Schaar算子
x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=-1)
y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=-1)

absx = cv.convertScaleAbs(x)
absy = cv.convertScaleAbs(y)

res = cv.addWeighted(absx, 0.5, absy, 0.5, 0)

plt.imshow(res, cmap=plt.cm.gray)
plt.show()
