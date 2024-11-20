# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:00:42 2024

@author: lenov
"""

# rotasi
import cv2
import numpy as np
img = cv2.imread("C:\\Users\\lenov\\Downloads\\doggie.jpeg")
print(img.shape)

baris, coloms, ghgh = img.shape

#MTranslasi = np.float32([[2, 0, 100],[0, 2, 50]])

#print(MTranslasi, '\n')

MRotasi = cv2.getRotationMatrix2D((coloms/2, baris/2,),90, 1)

print(MRotasi, '\n')


dst = cv2.warpAffine (img, MRotasi, (coloms, baris))
#dst = cv2.warpAffine (img, MTranslasi, (coloms, baris))
cv2.imshow("dst", dst) 
#cv2.imshow("rotasi", )

cv2.waitKey(0)
cv2.destroyAllWindows()