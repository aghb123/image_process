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
width = int(cap.get(3))
height = int(cap.get(4))

out = cv.VideoWriter("../image/out.avi", cv.VideoWriter_fourcc("M", "J", "P", "G"), 10, (width, height))

while True:
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()
