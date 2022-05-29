# 视频相关操作

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1 读取视频
cap = cv.VideoCapture("../image/DOG.wmv")

# 2 判断是否读取成功
# while cap.isOpened():
#     # 3 获取每一帧图像
#     ret, frame = cap.read()
#     # 4 是否获取成功
#     if ret:
#         cv.imshow("frame", frame)
#     if cv.waitKey(25) & 0xFF == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

# 3 图像保存
# width = int(cap.get(3))
# height = int(cap.get(4))
#
# out = cv.VideoWriter("../image/out.avi", cv.VideoWriter_fourcc("M", "J", "P", "G"), 10, (width, height))
#
# while True:
#     ret, frame = cap.read()
#     if ret:
#         out.write(frame)
#     else:
#         break
# cap.release()
# out.release()
# cv.destroyAllWindows()

# 4 图像追踪-meanshift/camshift
ret, frame = cap.read()  # 指定追踪目标
r, h, c, w = 197, 141, 0, 208
win = (c, r, w, h)
roi = frame[r:r + h, c:c + w]

hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

roi_hist = cv.calcHist([hsv_roi], [0], None, [180], [0, 180])

cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

term = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if ret:
        hst = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hst], [0], roi_hist, [0, 180], 1)
        # ret, win = cv.meanShift(dst, win, term)
        # x, y, w, h = win
        # print(win)
        # img2 = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)

        ret, win = cv.CamShift(dst, win, term)
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv.polylines(frame, [pts], True, 255, 2)

        cv.imshow("frame", img2)
        if cv.waitKey(60) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
