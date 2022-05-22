# 算数操作

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# x = np.uint8([250])
# y = np.uint8([10])
# print(cv.add(x, y))
# print(x + y)

rain = cv.imread("../image/rain.jpg")

view = cv.imread("../image/view.jpg")

img1 = cv.add(rain, view)
img2 = rain + view

# 图像混合
img3 = cv.addWeighted(view, 0.3, rain, 0.7, 0)
plt.imshow(img1[:, :, ::-1])
plt.show()
