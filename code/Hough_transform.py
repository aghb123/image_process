# 霍夫变换

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 霍夫线检测
img = cv.imread("../image/rili.jpg")
edges = cv.Canny(img, 50, 150)

lines = cv.HoughLines(edges, 0.8, np.pi / 180, 150)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0))

# 霍夫圆检测
star = cv.imread("../image/star.jpeg")

gray_img = cv.cvtColor(star, cv.COLOR_BGR2GRAY)
img = cv.medianBlur(gray_img, 7)

circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 200, param1=100, param2=50, minRadius=0, maxRadius=100)
print(circles.shape)
for i in circles[0]:
    cv.circle(star, (int(i[0]), int(i[1])), int(i[2]), (0, 255, 0), 2)
    cv.circle(star, (int(i[0]), int(i[1])), 2, (0, 255, 0), -1)

# plt.imshow(img, cmap=plt.cm.gray)
plt.imshow(star[:, :, ::-1])
plt.show()
