# coding: utf-8
import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import subprocess
import time

os.chdir('/home/workspace/heyinan/')

def get_imlist(path):
    '''

    获取文件夹下的图片，存为列表

    '''
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
img_paths = get_imlist('/home/workspace/muzhongkai/PCV/data/first500/')
num_words = 200
des_list = []  # 特征描述
des_matrix = np.zeros((1, 32))
start_time = time.time()
if img_paths != []:
    for im in img_paths:
        gray = cv2.imread(im, 0)
        orb = cv2.ORB_create()
        kp, des = orb.detectAndCompute(gray, None)  # detect key points and Calculate feature descriptors
        if len(kp) != 0:
            des_matrix = np.row_stack((des_matrix, des))  # combine matrix
        des_list.append(des)
else:
      raise ValueError(u'输入不合法')
end_time = time.time()
time_cost.append(np.round(end_time - start_time,2))
time_cost = pd.Series(time_cost)
print (time_cost)
des_matrix = des_matrix[1:, :]
des_matrix = np.vstack(des_list)
print ("starting kmeans trainning...")
kmeans = KMeans(n_clusters=num_words, random_state=33)
kmeans.fit(des_matrix)
pd.to_pickle(kmeans,'F:/kmeans_200_orb.pkl')
print ('train finished...')