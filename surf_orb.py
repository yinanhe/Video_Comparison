
import numpy as np
import cv2
from matplotlib import pyplot as plt

cv2.ocl.setUseOpenCL(False)
# 读入灰度图像
img1 = cv2.imread('F:/201411.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('F:/201412.jpg', cv2.IMREAD_GRAYSCALE)

# 创建orb特征检测器和描述符
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# 暴力匹配
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# 显示图像
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:40], img2, flags=2)
plt.imshow(img3), plt.show()


'''
import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

img = cv2.imread("F:/201411.jpg",0)
des_list1 = []  # 特征描述
des_matrix1 = np.zeros((1, 32))
des_list2 = []  # 特征描述
des_matrix2 = np.zeros((1, 32))
surf = cv2.xfeatures2d.SURF_create(1000)  # create sift class
surf.setExtended(True)  # 设置为128位
kp1, des1 = surf.detectAndCompute(img, None)

orb = cv2.ORB_create()
kp2 = orb.detect(img,None)
kp2,des2 = orb.compute(img,kp2)
#kp2, des2 = orb.detectAndCompute(img, None)

print ("kp1=",kp1)
print ("kp2=",kp2)
print ("des1=",des1)
print ("des2=",des2)
print(des1.ndim)
print(des2.ndim)
print(des1.shape)
print(des2.shape)
des_matrix1 = np.row_stack((des_matrix1, des1))
des_list1.append(des1)
#des_matrix2 = np.row_stack((des_matrix2, des2))
#des_list2.append(des2)
print(des_matrix1)
print(des_list1)
#print(des_matrix2)
#print(des_list2)
img2 = cv2.drawKeypoints(img,kp2,color=(0,255,0),flags=0)
plt.imshow(img2),plt.show()
'''