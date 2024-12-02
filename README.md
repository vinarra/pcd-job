# Image Manipulation

### Fungsi: imageRead(nama file)

Baris yang diberi komentar (baris 2-4):
Baris-baris ini awalnya dimaksudkan untuk membaca data gambar sebagai byte mentah. Baris-baris ini membuka berkas dalam mode biner ( 'rb'), membaca seluruh konten ( read()), menutup berkas ( close()), dan mengubah string byte menjadi array NumPy dengan bilangan bulat 8-bit yang tidak bertanda ( np.uint8).
### Baris 5:
img = cv.imread(filename): Baris ini menggunakan fungsi OpenCV cv.imreaduntuk langsung membaca gambar dari nama file yang ditentukan. Ini adalah cara yang lebih efisien dibandingkan dengan pendekatan yang dikomentari.
### Baris 6:
print(img.shape): Baris ini mencetak bentuk gambar yang dimuat sebagai tupel yang berisi tinggi, lebar, dan jumlah saluran (biasanya 3 untuk gambar RGB).
Baris yang diberi komentar (Baris 7):
#img = img.resize(400, 300, 3): Baris yang diberi komentar ini mencoba mengubah ukuran gambar ke ukuran tertentu (400x300 piksel dengan 3 saluran). Namun, pustaka yang digunakan tidak tepat untuk tugas ini. cv.resizeFungsi OpenCV dapat digunakan untuk mengubah ukuran.
### Baris 8:
img = cv.cvtColor(img, cv.COLOR_BGR2RGB): Baris ini mengonversi gambar dari format warna BGR (format bawaan OpenCV) ke format RGB. Hal ini karena RGB lebih umum digunakan untuk keperluan visualisasi.
### Baris 9:
return img: Baris ini mengembalikan gambar yang diproses (dikonversi ke RGB) dari fungsi.
Fungsi: showImage(judul, gambar)

### Baris 11:
cv.namedWindow(title, cv.WINDOW_AUTOSIZE): Baris ini membuat jendela untuk menampilkan gambar menggunakan cv.namedWindowfungsi OpenCV. Judul jendela diatur ke argumen yang diberikan ( title), dan cv.WINDOW_AUTOSIZEmemastikan jendela berubah ukuran secara otomatis agar sesuai dengan gambar.
### Baris 12:
cv.imshow(title, image): Baris ini menampilkan gambar ( image) di dalam jendela dengan judul yang ditentukan ( title) menggunakan fungsi OpenCV cv.imshow.
### Baris 13:
cv.waitKey(0): Baris ini menunggu tanpa batas waktu (0 milidetik) untuk penekanan tombol menggunakan fungsi OpenCV cv.waitKey. Ini membuat jendela tetap terbuka hingga pengguna menekan tombol untuk menutupnya.
Fungsi (dikomentari): imageWrite(nama file, gambar)

### Baris 15-17 (dikomentari):
Fungsi ini dimaksudkan untuk menulis gambar ke dalam berkas. Namun, saat ini komentarnya tidak ada. Fungsi ini membuka berkas dalam mode penulisan biner ( 'wb'), tetapi kode untuk menulis data gambar tidak ada.
Fungsi (dikomentari): convertToGray(gambar)

### Baris 19:
return (0.21 * image[:, :, 0] + 0.72 * image[:, :, 1] + 0.07 * image[:, :, 2]).astype(np.uint8): Baris ini mengonversi gambar RGB ke skala abu-abu menggunakan rata-rata tertimbang dari saluran merah, hijau, dan biru. Bobot (0,21, 0,72, dan 0,07) sesuai dengan koefisien luma Rekomendasi ITU-R BT.709 standar untuk memperkirakan persepsi manusia terhadap kecerahan. Hasilnya dikonversi ke array integer 8-bit tak bertanda ( np.uint8) yang merepresentasikan nilai skala abu-abu.
Fungsi: fullRangeLinearScaling(gambar)

### Baris 21:
max_value = np.max(image): Baris ini menemukan nilai piksel maksimum (intensitas) dalam gambar menggunakan np.maxfungsi NumPy.
Baris 22:
return ((255 / max_value) * image).astype(np.uint8): Baris ini melakukan penskalaan linier untuk menormalkan nilai piksel gambar ke rentang penuh (0-255). Baris ini menghitung faktor penskalaan dengan membagi 255 dengan nilai maksimum yang ditemukan sebelumnya. Faktor ini kemudian dikalikan dengan setiap nilai piksel dalam gambar. Hasilnya diubah menjadi array integer 8-bit yang tidak bertanda ( np.uint8) untuk mempertahankan rentang intensitas piksel yang diharapkan.
Fungsi: sliderCallBack(thresh)

### Baris 24:
`gambar = np.salin(gambarabu-abu

## Image Manipulation
```python
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
```
## Hasil
![image](https://github.com/user-attachments/assets/c33fa1f4-1bc5-41e9-a64e-8b72c3f4fd50)
