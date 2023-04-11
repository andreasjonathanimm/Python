import numpy as np

def main():
    array = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 0, 1, 0],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1, 0, 0, 0, 0]])
    kernel = np.ones((3,3),np.uint8)

    print("Original array: ")
    print(array)
    print("Kernel: ")
    print(kernel)
    print("Erosion: ")
    print(erosion(array, kernel))
    print("Dilation: ")
    print(dilation(array, kernel))
    print("Opening: ")
    print(opening(array, kernel))
    print("Closing: ")
    print(closing(array, kernel))


def erosion(array, kernel):
    """Erosion of an array with a kernel
    array: array to be eroded
    kernel: kernel to be used
    return: eroded array"""
    new_array = np.zeros((9,9),np.uint8)
    for i, row in enumerate(array, 1):
        for j, value in enumerate(row, 1):
            FLAG = True
            for k, row_kernel in enumerate(kernel):
                for l, value_kernel in enumerate(row_kernel):
                    if value_kernel == 1:
                        try:
                            if array[i-1+k][j-1+l] == 0:
                                FLAG = False # if any of the array is 0, then the new array is 0
                        except(IndexError):
                            FLAG = False
            if FLAG:
                new_array[i][j] = 1
    return new_array

def dilation(array, kernel):
    """Dilation of an array with a kernel
    array: array to be dilated
    kernel: kernel to be used
    return: dilated array"""

    new_array = np.zeros((9,9),np.uint8)
    for i, row in enumerate(array, 1):
        for j, value in enumerate(row, 1):
            FLAG = False
            for k, row_kernel in enumerate(kernel):
                for l, value_kernel in enumerate(row_kernel):
                    if value_kernel == 1:
                        try:
                            if array[i-1+k][j-1+l] == 1:
                                FLAG = True # if any of the array is 1, then the new array is 1
                        except(IndexError):
                            FLAG = False
            if FLAG:
                new_array[i][j] = 1
    return new_array

def opening(array, kernel):
    """Opening of an array with a kernel
    array: array to be opened
    kernel: kernel to be used
    return: opened array"""
    return dilation(erosion(array, kernel), kernel)

def closing(array, kernel):
    """Closing of an array with a kernel
    array: array to be closed
    kernel: kernel to be used
    return: closed array"""
    return erosion(dilation(array, kernel), kernel)

if __name__ == "__main__":
    main()