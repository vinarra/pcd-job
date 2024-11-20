# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:45:05 2024

@author: lenov
"""

import cv2 # Mengimpor OpenCV, sebuah library untuk pengolahan citra
import numpy as np #Mengimpor NumPy, digunakan untuk operasi array dan matriks
from matplotlib import pyplot as plt #Mengimpor submodule dari Matplotlib untuk visualisasi data

img = cv2.imread('C:\\Users\\lenov\\Pictures\\Camera Roll\\Saved Pictures\\apple.jpeg', 0) #Membaca citra grayscale

kernel = np.ones((3,3),np.uint8) #Membuat matriks 3x3 yang berisi angka 1, digunakan sebagai elemen struktur untuk operasi morfologi

erosion = cv2.erode(img,kernel,iterations=1) #Menerapkan operasi erosi pada citra dengan iterasi sebanyak 1 kali

titles = ['Normal Image', 'Erosion'] #Membuat judul yang akan ditampilkan

images = [img, erosion] #Membuat list untuk menyimpan kedua citra

cv2.imshow('Erosion', erosion) #Menampilkan hasil erosi
cv2.waitKey(0) #Menunggu 0 milidetik untuk menekan tombol pada jendela. 
cv2.destroyAllWindows() #Menutup semua jendela yang terbuka
