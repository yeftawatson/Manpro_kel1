import cv2
import numpy as np
import os

# Path to the directory containing the dataset images
dataset_path = 'dataset/'

# Load the image to compare
img_to_compare = cv2.imread('gambar2.jpg')

# Convert the image to grayscale
gray_img_to_compare = cv2.cvtColor(img_to_compare, cv2.COLOR_BGR2GRAY)

# Calculate the histogram of the image to compare
hist_to_compare = cv2.calcHist([gray_img_to_compare], [0], None, [256], [0, 256])
cv2.normalize(hist_to_compare, hist_to_compare, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

# Loop through each image in the dataset directory
for filename in os.listdir(dataset_path):
    if filename.endswith('.jpg'):
        # Load the image from the dataset directory
        dataset_img = cv2.imread(os.path.join(dataset_path, filename))
        
        # Convert the dataset image to grayscale
        gray_dataset_img = cv2.cvtColor(dataset_img, cv2.COLOR_BGR2GRAY)
        
        # Calculate the histogram of the dataset image
        hist_dataset_img = cv2.calcHist([gray_dataset_img], [0], None, [256], [0, 256])
        cv2.normalize(hist_dataset_img, hist_dataset_img, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        
        # Compare the histograms of the two images
        score = cv2.compareHist(hist_to_compare, hist_dataset_img, cv2.HISTCMP_CORREL)
        
        # Print the score and the name of the dataset image
        print(f'{filename}: {score}')
