# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 20:10:54 2024

@author: lenov
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def thinning(image):
    # Membuat salinan citra untuk hasil
    img = image.copy()
    # Struktur elemen untuk operasi thinning
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]], np.uint8)

    while True:
        # Menghitung jumlah piksel tetangga
        eroded = cv2.erode(img, kernel)
        temp = cv2.dilate(eroded, kernel)
        temp = cv2.subtract(img, temp)
        
        img = eroded.copy()
        img = cv2.subtract(img, temp)

        # Jika tidak ada perubahan, keluar dari loop
        if cv2.countNonZero(temp) == 0:
            break

    return img

# Membaca citra
img = cv2.imread('C:\\Users\\lenov\\Pictures\\Camera Roll\\Saved Pictures\\apple.jpeg', 0)

# Mengubah citra ke biner
_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Melakukan thinning
thinned_img = thinning(binary_img)

# Menampilkan citra
titles = ['Original Image', 'Binary Image', 'Thinned Image']
images = [img, binary_img, thinned_img]

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
