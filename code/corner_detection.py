# 角点检测

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../image/chessboard.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(gray)
plt.imshow(gray, 'gray')
plt.show()
gray = np.float32(gray)
print(gray)
plt.imshow(gray)
plt.show()

# Harris方法
dst = cv.cornerHarris(gray, 2, 3, 0.04)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

# shi-tomas方法
img = cv.imread("../image/tv.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray, 1000, 0.01, 10)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (int(x), int(y)), 2, (0, 0, 255), -1)

# sift方法
img = cv.imread("../image/tv.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()

kp, des = sift.detectAndCompute(gray, None)

cv.drawKeypoints(img, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# fast算法
img = cv.imread("../image/tv.jpg")

fast = cv.FastFeatureDetector_create(threshold=30)

kp = fast.detect(img, None)

img2 = cv.drawKeypoints(img, kp, None, color=(0, 0, 255))

fast.setNonmaxSuppression(0)

kp = fast.detect(img, None)

img3 = cv.drawKeypoints(img, kp, None, color=(0, 0, 255))

# ORB算法
img = cv.imread("../image/tv.jpg")

orb = cv.ORB_create(nfeatures=5000)

kp, des = orb.detectAndCompute(img, None)

print(des)

img2 = cv.drawKeypoints(img, kp, None, flags=0)

plt.imshow(img2[:, :, ::-1])
plt.show()
