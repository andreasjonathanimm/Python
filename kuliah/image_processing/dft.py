"""Discrete Fourier Transform Algorithm"""
import numpy as np

# 1D DFT: F(k) = sum(f(n) * exp(-j*2*pi*k*x/N), n=0..N-1) where k=0..N-1
# 2D DFT: F(k,l) = sum(f(x,y) * exp(-j*2*pi*(k*x/N + l*y/N)), x=0..N-1, y=0..N-1) where k=0..N-1, l=0..N-1
# Inverse DFT: f(n) = 1/N * sum(F(k) * exp(j*2*pi*k*x/N), k=0..N-1) where n=0..N-1
# Inverse 2D DFT: f(x,y) = 1/N^2 * sum(F(k,l) * exp(j*2*pi*(k*x/N + l*y/N)), k=0..N-1, l=0..N-1) where x=0..N-1, y=0..N-1

# Important formulas:
# e^jn = -1
# e^-jn = 1
# e^j*pi/2 = j
# e^-j*pi/2 = -j
# e^j*2pi = 1
# e^j*3pi = -1
# e^-j*3pi/2 = j
# e^-j*a*pi/2 = -j
# e^-j*tetra = cos(tetra) - j*sin(tetra)
# e^j*tetra = cos(tetra) + j*sin(tetra)

# Kernel of a 4-point DFT
# [1, 1, 1, 1]
# [1, 1j, -1, -1j]
# [1, -1, 1, -1]
# [1, -1j, -1, 1j]

# 1D DFT: F[k] = kernel * f(x)
# 2D DFT: F[k,l] = kernel * kernel^T * f(x,y)

# Example: 1D DFT
sequence = np.array([0, 1, 2, 3])

# Answer: F[k] = kernel * f(x)
kernel = np.array([[1, 1, 1, 1], [1, 1j, -1, -1j], [1, -1, 1, -1], [1, -1j, -1, 1j]])
print(kernel @ sequence) # [6, -2 + 2j, -2, -2 - 2j]

# Example: 2D DFT
grayscale = np.ones((4, 4))

# Answer: F[k,l] = kernel * kernel^T * f(x,y)
kernel = np.array([[1, 1, 1, 1], [1, 1j, -1, -1j], [1, -1, 1, -1], [1, -1j, -1, 1j]])
print(kernel @ grayscale @ kernel.T) # [[16, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Reverse DFT: x[n] = 1/N * kernel^T * F[k]
kernel = np.array([[1, 1, 1, 1], [1, 1j, -1, -1j], [1, -1, 1, -1], [1, -1j, -1, 1j]])
sequence = np.array([6, -2 + 2j, -2, -2 - 2j])
print(1/4 * kernel.T @ sequence) # [0, 1, 2, 3]

# Reverse 2D DFT: x[n] = 1/N^2 * kernel^T * kernel^T * F[k,l]
kernel = np.array([[1, 1, 1, 1], [1, 1j, -1, -1j], [1, -1, 1, -1], [1, -1j, -1, 1j]])
grayscale = np.array([[16, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

# Exercise:
sequence = np.array([[2, 3], [3, 2]])
def dft2d(sequence: np.ndarray) -> np.ndarray:
    """Compute the DFT of a 2D sequence"""
    # Get the size of the input sequence
    N, M = len(sequence), len(sequence[0])

    # Initialize the output sequence
    new_sequence = np.zeros_like(sequence)

    # Iterate over the input sequence
    for idx, row in enumerate(sequence):
        for jdx, col in enumerate(row):
            print("=============")
            print("idx, jdx: ", idx, jdx)
            # Iterate over the input sequence again
            for kdx, new_row in enumerate(sequence):
                for ldx, new_col in enumerate(new_row):
                    # Compute the DFT of the input sequence
                    new_sequence[idx, jdx] += sequence[kdx, ldx] * np.exp(-1j * 2 * np.pi * (kdx * idx / N + ldx * jdx / M))
                    print("kdx, ldx, sum: ", kdx, ldx, new_sequence[idx, jdx])
            print("value: ", new_sequence[idx, jdx])
            print("=============")
    return new_sequence

print("Sequence: ")
print(sequence) # [[2, 3], [3, 2]]
print(dft2d(sequence)) # [[10, 0], [0, -2]]

# Exercise 2:
sequence = np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]])
print("Sequence 2:")
print(sequence) # [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
print(dft2d(sequence)) # [[10, 0, 0], [0, 0, 1], [0, 1, 0]]