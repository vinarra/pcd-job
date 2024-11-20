# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 08:51:46 2024

@author: lenov
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\lenov\\Pictures\\Camera Roll\\Saved Pictures\\fruit.jpeg', 0)
imgO = cv2.imread('C:\\Users\\lenov\\Pictures\\Camera Roll\\Saved Pictures\\apple.jpeg', 0)
imgC = cv2.imread('C:\\Users\\lenov\\Pictures\\Camera Roll\\Saved Pictures\\bana.jpeg', 0)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(imgO, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(imgC, cv2.MORPH_CLOSE, kernel)

titles = ['Normal Image', 'Erosion',
          'Dilation', 'Before Opening', 
          'Opening', 'Before Closing', 'Closing']

images = [img, erosion, dilation, imgO, opening, imgC, closing]

cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)
cv2.waitKey()
cv2.destroyAllWindows()
# =============================================================================
# for i in range(7):
#     plt.subplot(2,5,i+1),plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
# =============================================================================



