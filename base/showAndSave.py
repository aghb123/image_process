# 图像的显示与保存
import cv2
import matplotlib.pyplot as plt

# lena = cv2.imread('lena.jpg')
lena = cv2.imread('lena.jpg', 0)
# cv2.imshow("image", lena)
# cv2.waitKey(0)

# matplotlib中展示
# plt.imshow(lena[:,:,::-1])
plt.imshow(lena, cmap=plt.cm.gray)

plt.show()

# 图像保存
cv2.imwrite("../image/lena.png", lena)
