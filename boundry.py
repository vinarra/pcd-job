# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 20:28:46 2024

@author: lenov
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def boundary_extraction(image):
    # Membuat salinan citra untuk hasil
    img = image.copy()
    
    # Struktur elemen untuk operasi boundary extraction
    kernel = np.ones((3, 3), np.uint8)

    # Melakukan dilasi dan kemudian mengurangi citra asli
    dilated = cv2.dilate(img, kernel, iterations=1)
    boundary = cv2.subtract(dilated, img)

    return boundary

# Membaca citra
img = cv2.imread('C:\\Users\\lenov\\Pictures\\Camera Roll\\Saved Pictures\\apple.jpeg', 0)

# Mengubah citra ke biner
_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Melakukan boundary extraction
boundary_img = boundary_extraction(binary_img)

# Menampilkan citra
titles = ['Original Image', 'Binary Image', 'Boundary Extracted Image']
images = [img, binary_img, boundary_img]

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

