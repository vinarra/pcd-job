# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:50:42 2024

@author: lenov
"""

#konversi warna ke Abu-abu 
import cv2 
import numpy as np


img = cv2.imread("C://Users//lenov//Pictures//Camera Roll//Saved Pictures//images.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(tresh, BW) = cv2.threshold(gray, 127, 255, cv2.TH RESH_BINARY)

cv2.imshow("gray", gray)
cv2.imshow("BW", BW) 

cv2.waitKey(0)
cv2.destroyAllWindows()