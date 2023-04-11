"""2D-Discrete Wavelet Transform (DWT) and Inverse DWT for transforming RGB image into approximation and detail coefficients."""
import numpy as np # pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
import pywt # pip install pywavelets
import cv2 # pip install opencv-python

img = cv2.imread('./image.png', cv2.IMREAD_COLOR)

# Wavelet transformation on RGB image
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Original image
plt.imshow(img)
plt.title('Original Image')
plt.show()

# Retrieve approximation and detail coefficients for each channel (R, G, B)
r = pywt.dwt2(img[:,:,0], 'haar')
g = pywt.dwt2(img[:,:,1], 'haar')
b = pywt.dwt2(img[:,:,2], 'haar')

a = np.dstack((r[0], g[0], b[0])) # Approximation
h = np.dstack((r[1][0], g[1][0], b[1][0])) # Horizontal detail
v = np.dstack((r[1][1], g[1][1], b[1][1])) # Vertical detail
d = np.dstack((r[1][2], g[1][2], b[1][2])) # Diagonal detail

# Normalize approximation and detail coefficients
a = (a - a.min()) / (a.max() - a.min())
h = (h - h.min()) / (h.max() - h.min())
v = (v - v.min()) / (v.max() - v.min())
d = (d - d.min()) / (d.max() - d.min())

# Plot approximation and detail coefficients
fig, axs = plt.subplots(2, 2)
axs[0, 0].imshow(a)
axs[0, 0].set_title('Approximation')
axs[0, 1].imshow(h)
axs[0, 1].set_title('Horizontal detail')
axs[1, 0].imshow(v)
axs[1, 0].set_title('Vertical detail')
axs[1, 1].imshow(d)
axs[1, 1].set_title('Diagonal detail')
plt.show()

# Apply DWT on approximation coefficients
r = pywt.dwt2(a[:,:,0], 'haar')
g = pywt.dwt2(a[:,:,1], 'haar')
b = pywt.dwt2(a[:,:,2], 'haar')

a = np.dstack((r[0], g[0], b[0])) # Approximation
h = np.dstack((r[1][0], g[1][0], b[1][0])) # Horizontal detail
v = np.dstack((r[1][1], g[1][1], b[1][1])) # Vertical detail
d = np.dstack((r[1][2], g[1][2], b[1][2])) # Diagonal detail

# Normalize approximation and detail coefficients
a = (a - a.min()) / (a.max() - a.min())
h = (h - h.min()) / (h.max() - h.min())
v = (v - v.min()) / (v.max() - v.min())
d = (d - d.min()) / (d.max() - d.min())

# Plot approximation and detail coefficients
fig, axs = plt.subplots(2, 2)
axs[0, 0].imshow(a)
axs[0, 0].set_title('Approximation')
axs[0, 1].imshow(h)
axs[0, 1].set_title('Horizontal detail')
axs[1, 0].imshow(v)
axs[1, 0].set_title('Vertical detail')
axs[1, 1].imshow(d)
axs[1, 1].set_title('Diagonal detail')
plt.show()
