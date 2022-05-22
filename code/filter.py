# 滤波处理

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

dogsp = cv.imread("../image/dogsp.jpeg")
dogGauss = cv.imread("../image/dogGauss.jpeg")

# 均值滤波
dog = cv.blur(dogsp, (5, 5))

# 高斯滤波
dog1 = cv.GaussianBlur(dogGauss, (3, 3), 1)

# 中值滤波
dog2 = cv.medianBlur(dogsp, 3)

plt.imshow(dog2[:, :, ::-1])
plt.show()
