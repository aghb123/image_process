# 人脸检测

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../image/yangzi.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 实例化检测器
face_cas = cv.CascadeClassifier("../image/haarcascade_frontalface_default.xml")
face_cas.load("../image/haarcascade_frontalface_default.xml")

eyes_cas = cv.CascadeClassifier("../image/haarcascade_eye.xml")
eyes_cas.load("../image/haarcascade_eye.xml")

# 人脸检测
face_rects = face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

# 绘制人脸
for facerect in face_rects:
    x, y, w, h = facerect
    cv.rectangle(img, (x, y), (x + w, y + h), 255, 3)
    roi_color = img[y:y + h, x:x + w]
    roi_gray = gray[y:y + h, x:x + w]
    eyes = eyes_cas.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), 255, 3)

plt.imshow(img[:, :, ::-1])
plt.show()
