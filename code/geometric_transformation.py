# 图像的几何变换

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.rc("font", family="Microsoft YaHei")

kids = cv.imread("../image/kids.jpg")
print(kids.shape)
# 绝对尺寸缩放
rows, cols = kids.shape[:2]
res = cv.resize(kids, (2 * cols, 2 * rows))
# 相对尺寸缩放
res1 = cv.resize(kids, None, fx=0.5, fy=0.5)

# 平移
M = np.float32([[1, 0, 100], [0, 1, 50]])
res2 = cv.warpAffine(kids, M, (2 * cols, 2 * rows))

# 图像旋转
M = cv.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)  # 先获取旋转矩阵
dst = cv.warpAffine(kids, M, (cols, rows))

# 仿射变换
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[100, 100], [200, 50], [100, 250]])
M = cv.getAffineTransform(pts1, pts2)
res3 = cv.warpAffine(kids, M, (cols, rows))

# 投射变换
pts3 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])  # 任意三点不共线
pts4 = np.float32([[100, 145], [300, 100], [80, 290], [310, 300]])
T = cv.getPerspectiveTransform(pts3, pts4)
res4 = cv.warpPerspective(kids, T, (cols, rows))

# 图像金字塔
imgUp = cv.pyrUp(kids)  # 上采样
imgDown = cv.pyrDown(kids)  # 下采样

# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), dpi=100)
# axes[0].imshow(kids[:, :, ::-1])
# axes[0].set_title("原图")
# axes[1].imshow(dst[:, :, ::-1])
# axes[1].set_title("旋转后结果")
plt.imshow(imgDown[:, :, ::-1])
plt.show()
