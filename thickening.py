import cv2
import numpy as np
from matplotlib import pyplot as plt

def thickening(image): 
    # Membuat salinan citra untuk hasil
    img = image.copy()
    
    # Struktur elemen untuk operasi thickening
    kernel = np.ones((3, 3), np.uint8)
    
    # Melakukan dilasi beberapa kali
    dilated = cv2.dilate(img, kernel, iterations=1)
    
    return dilated

# Membaca citra
img = cv2.imread('C:\\Users\\lenov\\Pictures\\Camera Roll\\Saved Pictures\\apple.jpeg', 0)

# Mengubah citra ke biner
_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Melakukan thickening
thickened_img = thickening(binary_img)

# Menampilkan citra
titles = ['Original Image', 'Binary Image', 'Thickened Image']
images = [img, binary_img, thickened_img]

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
