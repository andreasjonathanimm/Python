import numpy as np
import math as m
from hist_eq import hist_eq

# Contrast Limited Adaptive Histogram Equalization
def clahe(arr, r, k, c):
    # r is a range of intensity values [n, m]
    # k is the size of the window
    # c is the clip limit
    # Calculate the histogram equalization for each window
    new_img = np.zeros((len(arr), len(arr[0])))
    for i in range(len(arr) // k):
        for j in range(len(arr[0]) // k):
            # Create the window
            window = np.array([[0 for x in range(k)] for y in range(k)])

            # Take the values from the original image and put them in the window
            for x in range(k):
                for y in range(k):
                    window[x][y] = arr[i * k + x][j * k + y]

            # Calculate the histogram equalization for the window
            new_window = hist_eq(window, r, c)

            # Put the values from the window in the new image
            for x in range(k):
                for y in range(k):
                    new_img[i * k + x][j * k + y] = new_window[x][y]
    return new_img

def main():
    # Read the array
    arr = np.array([[10,10,10,10,10,10],[10,10,11,11,10,10],[10,11,11,11,11,10],[10,11,11,11,11,10],[10,10,11,11,10,10],[10,10,10,10,10,10]])
    print(arr)

    # Call the function
    new_img = clahe(arr, [0, 15], 3, 2)
    print(new_img)

if __name__ == "__main__":
    main()