# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:52:59 2024

@author: lenov
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\lenov\\Pictures\\Camera Roll\\Saved Pictures\\study.jpg')

blur1 = cv2.blur(img,(3,3))
blur2 = cv2.GaussianBlur(img,(3,3),0)
median = cv2.medianBlur(img,3)    
blur3 = cv2.bilateralFilter(img,9,75,75)

titles = ['Gambar Asli', 'Averaging',
          'Gaussian Blur', 'Bilateral Blur',
          'Median Blur']

images = [img, blur1, blur2, blur3, median]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()