# 图像基础处理
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = np.zeros((256, 256, 3), np.uint8)

img[100, 100] = (0, 0, 255)
plt.imshow(img[:, :, ::-1])
# plt.show()

# 图像的属性
print(img.shape)
print(img.dtype)
print(img.size)

img = cv.imread("../image/lena.jpg")
# 图像通道的拆分与合并
b, g, r = cv.split(img)
# plt.imshow(b, cmap=plt.cm.gray)
# plt.show()
print(b.shape)
img = cv.merge((b, g, r))
# plt.imshow(img[:, :, ::-1])
# plt.show()

# 色彩空间的改变

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # BGR->GRAY
# plt.imshow(gray, cmap=plt.cm.gray)
# plt.show()
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # BGR->HSV
plt.imshow(hsv)
plt.show()
