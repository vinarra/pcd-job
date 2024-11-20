# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:17:18 2024

@author: lenov
"""

# skala

import cv2

img = cv2.imread('C:\\Users\\lenov\\Downloads\\doggie.jpeg')

dstSkala = cv2.resize(img, None, fx=2.5, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("img",img)
cv2.imshow("dstSkala",dstSkala)

cv2.waitKey(0)
cv2.destroyAllWindows()