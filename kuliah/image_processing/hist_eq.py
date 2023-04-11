import numpy as np
import math as m

# Histogram equalization
def hist_eq(arr, r):
    # r is a range of intensity values [n, m]
    # Calculate the histogram
    hist = [0 for x in range(r[1])]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            hist[arr[i][j]] += 1

    # Calculate the probability of each intensity
    prob = [0 for x in range(r[1])]
    for i in range(r[1]):
        prob[i] = hist[i] / (len(arr) * len(arr[0]))
    
    # Calculate the cumulative distribution function
    cdf = [0 for x in range(r[1])]
    cdf[0] = prob[0]
    for i in range(1, r[1]):
        cdf[i] = cdf[i-1] + prob[i]

    # Calculate the new intensity
    new_int = [0 for x in range(r[1])]
    for i in range(r[1]):
        new_int[i] = round(r[1] * cdf[i])

    # Create the new image
    new_img = np.zeros((len(arr), len(arr[0])))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            new_img[i][j] = new_int[arr[i][j]]

    return new_img

def hist_eq(arr, r, c):
    # r is a range of intensity values [n, m]
    # c is the clip limit
    # Calculate the histogram
    hist = [0 for x in range(r[1])]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            hist[arr[i][j]] += 1

    # Calculate the difference between the number of pixels and the clip limit
    diff = [0 for x in range(r[1])]
    for i in range(r[1]):
        diff[i] = hist[i] - c
        if diff[i] < 0:
            diff[i] = 0

    # Calculate the number of pixels to be distributed
    for i in range(r[1]):
        hist[i] -= diff[i]

    # Calculate the probability of each intensity
    prob = [0 for x in range(r[1])]
    for i in range(r[1]):
        prob[i] = hist[i] / (len(arr) * len(arr[0]))

    # Calculate the cumulative distribution function
    cdf = [0 for x in range(r[1])]
    cdf[0] = prob[0]
    for i in range(1, r[1]):
        cdf[i] = cdf[i-1] + prob[i]

    # Calculate the new intensity
    new_int = [0 for x in range(r[1])]
    for i in range(r[1]):
        new_int[i] = round(r[1] * cdf[i])

    # Create the new image
    new_img = np.zeros((len(arr), len(arr[0])))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            new_img[i][j] = new_int[arr[i][j]]

    return new_img

def main():
    # Read the array
    arr = np.array([[10,10,10,10,10,10],[10,10,11,11,10,10],[10,11,11,11,11,10],[10,10,11,11,10,10],[10,10,10,10,10,10]])
    print(arr)

    # Call the function
    new_img = hist_eq(arr, [0, 15])
    print(new_img)

if __name__ == "__main__":
    main()