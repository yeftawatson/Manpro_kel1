import cv2
import numpy as np
import os

# Inisialisasi lokasi dataset
dataset_path = 'dataset'

# Load gambar input
img_to_compare = cv2.imread('gambar1.jpg')

# convert gambar grayscale
gray_img_to_compare = cv2.cvtColor(img_to_compare, cv2.COLOR_BGR2GRAY)

# Calculate histogram
hist_to_compare = cv2.calcHist([gray_img_to_compare], [0], None, [256], [0, 256])
cv2.normalize(hist_to_compare, hist_to_compare, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

# Looping membandingkan gambar selama gambar masih ada di dataset
for filename in os.listdir(dataset_path):
    if filename.endswith('.jpg'):
        # Load gambar
        dataset_img = cv2.imread(os.path.join(dataset_path, filename))
        
        # Ubah menjadi grayscale
        gray_dataset_img = cv2.cvtColor(dataset_img, cv2.COLOR_BGR2GRAY)
        
        # Hitung histogram
        hist_dataset_img = cv2.calcHist([gray_dataset_img], [0], None, [256], [0, 256])
        cv2.normalize(hist_dataset_img, hist_dataset_img, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        
        # Membandingkan histogram
        score = cv2.compareHist(hist_to_compare, hist_dataset_img, cv2.HISTCMP_CORREL)
        
        # Konversi nilai similarity
        percentage_score = score * 100
        
        # Print output
        print(f'{filename}: {percentage_score:.2f}%')
