# 模板匹配

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../image/wulin.jpeg")
template = cv.imread("../image/bai.jpeg")

# 模板匹配
res = cv.matchTemplate(img, template, cv.TM_CCORR)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
h, w = template.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)

cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

plt.imshow(img[:, :, ::-1])
# plt.imshow(res, cmap=plt.cm.gray)
plt.show()
