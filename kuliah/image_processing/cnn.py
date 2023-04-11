import numpy as np
import math as m

# convolution using CNN
# initial array
arr = np.array([[1, 1, 2, 2, 1, 1], [10, 10, 10, 10, 10, 10], [100, 100, 10, 10, 100, 100], [1, 1, 100, 100, 1, 1], [1, 1, 2, 2, 1, 1], [1, 1, 2, 2, 1, 1]])
n = len(arr)
conv_size = [2, 6]
print("Initial array: ")
print(arr)
print()

# convolution kernel
# (n/2, n/2) kernel
for c in conv_size:
    print("Convolution size: ", c)
    kernel = np.array([[1, 1, 1], [0, 0, 0], [1, 1, 1]])
    print(kernel)

    # convolution matrix
    conv = np.zeros((c, c))
    if c == n:
        arr2 = np.zeros((n+2, n+2))
        arr2[1:n+1, 1:n+1] = arr
        arr = arr2
    for i in range(0, c):
        for j in range(0, c):
            conv[i, j] = np.sum(arr[i:i+3, j:j+3]*kernel)

    print("Convolution matrix: ")
    print(conv)

    print("Convolution matrix shape: ")
    print(conv.shape)

    print("Convolution matrix size: ")
    print(conv.size)
    print()

print("End of program")