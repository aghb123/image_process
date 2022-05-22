# 滤波处理

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

dogsp = cv.imread("../image/dogsp.jpeg")
dogGauss = cv.imread("../image/dogGauss.jpeg")

# 均值滤波
dog = cv.blur(dogsp, (5, 5))

plt.imshow(dog[:, :, ::-1])
plt.show()
