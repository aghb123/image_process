# 直方图

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../image/cat.jpeg", 0)

# 直方图
hist = cv.calcHist([img], [0], None, [256], [0, 256])

# 掩膜
mask = np.zeros(img.shape[:2], np.uint8)
mask[400:650, 200:500] = 1

mask_img = cv.bitwise_and(img, img, mask=mask)

mask_hist = cv.calcHist([img], [0], mask, [256], [0, 256])

# 直方图均衡化
dst = cv.equalizeHist(img)

# 自适应的直方图均衡化
cl = cv.createCLAHE(2.0, (8, 8))

clahe = cl.apply(img)

# plt.figure(figsize=(10, 8))
# plt.plot(mask_hist)
plt.imshow(clahe, cmap=plt.cm.gray)
plt.show()
