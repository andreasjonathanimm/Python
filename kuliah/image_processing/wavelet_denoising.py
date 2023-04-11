"""Wavelet based denoising of image"""
import numpy as np # pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
import pywt # pip install pywavelets
import cv2 # pip install opencv-python

# Read image
img = cv2.imread('./noised_image.png', cv2.IMREAD_GRAYSCALE)

# Original image
plt.figure()
plt.imshow(img, cmap='gray')
plt.title('Original image')
plt.axis('off')
plt.show()

# Apply 3-level DWT2D on image
coeffs = pywt.dwt2(img, 'db1') # db1 = Daubechies wavelet, level 1
coeffs = pywt.dwt2(coeffs[0], 'db1') # level 2
coeffs = pywt.dwt2(coeffs[0], 'db1') # level 3

# Level 3
# Find threshold on detail components
thr = pywt.threshold(coeffs[1], np.std(coeffs[1]), mode='hard')

# Apply threshold on detail components
coeffs = list(coeffs)
coeffs[1] = thr

# Level 2
# Find threshold on detail components
thr = pywt.threshold(coeffs[1], np.std(coeffs[1]), mode='hard')

# Apply threshold on detail components
coeffs = list(coeffs)
coeffs[1] = thr

# Level 1
# Find threshold on detail components
thr = pywt.threshold(coeffs[1], np.std(coeffs[1]), mode='hard')

# Apply threshold on detail components
coeffs = list(coeffs)
coeffs[1] = thr

# Reconstruct image
img_denoised = pywt.idwt2(coeffs, 'db1')

# Denoised image
plt.figure()
plt.imshow(img_denoised, cmap='gray')
plt.title('Denoised image')
plt.axis('off')
plt.show()