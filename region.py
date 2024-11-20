import cv2
import numpy as np
from matplotlib import pyplot as plt

def region_filling(image):
    # Membuat salinan citra untuk hasil
    img = image.copy()
    
    # Menggunakan flood fill untuk mengisi area kosong
    h, w = img.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Menentukan titik awal untuk flood fill
    start_point = (0, 0)  # Ubah titik ini sesuai kebutuhan
    
    # Melakukan flood fill
    cv2.floodFill(img, mask, start_point, 255)

    return img

# Membaca citra
img = cv2.imread('C:\\Users\\lenov\\Pictures\\Camera Roll\\Saved Pictures\\apple.jpeg', 0)

# Mengubah citra ke biner
_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)

# Melakukan region filling
filled_img = region_filling(binary_img)

# Menampilkan citra
titles = ['Original Image', 'Binary Image', 'Region Filled Image']
images = [img, binary_img, filled_img]

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
