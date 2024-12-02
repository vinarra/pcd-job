# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:19:49 2024

@author: lenov
"""

# works with raw images only
import cv2
import numpy as np, cv2 as cv #pustaka OpenCV yang digunakan untuk memproses gambar.
from matplotlib import pyplot as plt #digunakan untuk visualisasi gambar


def imageRead(filename):
    #readFile = open(filename, 'rb')
    #img_str = readFile.read()
    #readFile.close()
    #img = np.array(bytearray(img_str), np.uint8)
    img = cv2.imread("C:\\Users\\lenov\\Downloads\\ggr.png")
    print(img.shape) #Menampilkan ukuran gambar
    #img = img.resize(400, 300, 3)  # shape height, width, 3 
    img = cv2.cvtColor(img, cv.COLOR_BGR2RGB) #Mengkonversi gambar 
    return img


# def imageWrite(filename, image):
#     writeFile = open(filename, 'wb')


def showImage(title, image):
    cv2.namedWindow(title, cv.WINDOW_AUTOSIZE) #Membuat jendela dengan nama title yang ukurannya disesuaikan secara otomatis 
    cv2.imshow(title, image) #Menampilkan gambar yang diberikan dalam jendela dengan nama title.
    cv2.waitKey(0)


# works with gray images
def convertToGray(image): #Mengkonversi gambar berwarna (RGB) menjadi gambar grayscale.
    return (0.21 * image[:, :, 0] + 0.72 * image[:, :, 1] + 0.07 * image[:, :, 2]).astype(np.uint8) #Mengubah tipe data gambar menjadi uint8


def fullRangeLinearScaling(image): #memastikan bahwa nilai piksel berada dalam rentang 0 hingga 255.
    max_value = np.max(image) #Mencari nilai piksel maksimum dalam gambar
    return ((255 / max_value) * image).astype(np.uint8) #Menyesuaikan gambar sehingga nilai piksel maksimum menjadi 255, menskalakan seluruh gambar

def sliderCallBack(thresh):
    image = np.copy(grayImage) #Membuat salinan dari gambar 
    truthImage = image < thresh
    image[truthImage] = 0 #Menetapkan piksel yang lebih kecil dari threshold menjadi 0 (hitam
    image[~truthImage] =255 #Menetapkan piksel yang lebih besar dari threshold menjadi 255 (putih).
    # image[not truthImage] = 255
    cv2.imshow('Thresholding', image)


def thresholdGrayImage():
    cv2.namedWindow('Thresholding', cv.WINDOW_AUTOSIZE)
    cv2.createTrackbar('Threshold', 'Thresholding',128, 255, sliderCallBack) #ntuk memperbarui gambar.
    cv2.waitKey(0) #Menunggu input dari pengguna untuk menutup jendela.

inputImage = imageRead("C:\\Users\\lenov\\Downloads\\ggr.png")


grayImage = convertToGray(inputImage) #Mengkonversi gambar yang dibaca menjadi grayscale.
showImage('gambar', inputImage)
#thresholdGrayImage()
#out = cv.adaptiveThreshold(grayImage, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,7,2)
#showImage('Equalization', cv.equalizeHist(grayImage))
#showImage('adaptive', out)