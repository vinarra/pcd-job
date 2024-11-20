# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:19:49 2024

@author: lenov
"""

# works with raw images only
import numpy as np, cv2 as cv
from matplotlib import pyplot as plt


def imageRead(filename):
    #readFile = open(filename, 'rb')
    #img_str = readFile.read()
    #readFile.close()
    #img = np.array(bytearray(img_str), np.uint8)
    img = cv.imread(filename)
    print(img.shape)
    #img = img.resize(400, 300, 3)  # shape height, width, 3
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return img


# def imageWrite(filename, image):
#     writeFile = open(filename, 'wb')


def showImage(title, image):
    cv.namedWindow(title, cv.WINDOW_AUTOSIZE)
    cv.imshow(title, image)
    cv.waitKey(0)


# works with gray images
def convertToGray(image):
    return (0.21 * image[:, :, 0] + 0.72 * image[:, :, 1] + 0.07 * image[:, :, 2]).astype(np.uint8)


def fullRangeLinearScaling(image):
    max_value = np.max(image)
    return ((255 / max_value) * image).astype(np.uint8)

def sliderCallBack(thresh):
    image = np.copy(grayImage)
    truthImage = image < thresh
    image[truthImage] = 0
    image[~truthImage] =255
    # image[not truthImage] = 255
    cv.imshow('Thresholding', image)


def thresholdGrayImage():
    cv.namedWindow('Thresholding', cv.WINDOW_AUTOSIZE)
    cv.createTrackbar('Threshold', 'Thresholding',128, 255, sliderCallBack)
    cv.waitKey(0)

inputImage = imageRead("C:\\Users\\lenov\\Downloads\\ggr.png")

grayImage = convertToGray(inputImage)
showImage('gambar', inputImage)
#thresholdGrayImage()
#out = cv.adaptiveThreshold(grayImage, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,7,2)
#showImage('Equalization', cv.equalizeHist(grayImage))
#showImage('adaptive', out)