"""Wavelet based compression of image"""
import numpy as np # pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
import pywt # pip install pywavelets
import cv2 # pip install opencv-python

# Read image
img = cv2.imread('./image.png', cv2.IMREAD_COLOR)

# Convert image to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Original image
plt.figure()
plt.imshow(img, cmap='gray')
plt.title('Original image')
plt.axis('off')
plt.show()

# Wavelet compression
coeffs = pywt.wavedec2(img, 'db1', level=4)
coeffs_sort = sorted(coeffs, key=lambda x: np.prod(x))

for keep in (0.1, 0.05, 0.01, 0.005):
    coeffs_trunc = []
    n_coeffs = 0
    n_coeffs_total = sum(len(c) for c in coeffs_sort)
    for c in coeffs_sort:
        coeffs_trunc.append(c)
        n_coeffs += len(c)
        if n_coeffs >= n_coeffs_total * keep:
            break

    img_trunc = pywt.waverec2(coeffs_trunc, 'db1')
    plt.figure()
    plt.imshow(img_trunc, cmap='gray')
    plt.title('Wavelet compression, keep = %g' % keep)
    plt.axis('off')
    plt.show()