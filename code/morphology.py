# 形态学操作

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 腐蚀
img = cv.imread("../image/letter.png")

kenel = np.ones((5, 5), np.uint8)  # 创建核结构
img2 = cv.erode(img, kenel)

# 膨胀
img3 = cv.dilate(img, kenel)

# 开运算 去除噪点
open = cv.imread("../image/letteropen.png")
kenel = np.ones((10, 10), np.uint8)
cvopen = cv.morphologyEx(open, cv.MORPH_OPEN, kenel)

# 闭运算 去除孔洞
close = cv.imread("../image/letterclose.png")
cvclose = cv.morphologyEx(close, cv.MORPH_CLOSE, kenel)

# 黑帽和礼帽
top = cv.morphologyEx(open, cv.MORPH_TOPHAT, kenel)  # 礼帽 获取比邻近点更亮的轮廓
black = cv.morphologyEx(close, cv.MORPH_BLACKHAT, kenel)  # 黑帽 获取比邻近点更暗的轮廓
plt.imshow(black[:, :, ::-1])
plt.show()
