arr = [10, 110, 10, 10, 100, 10, 100, 101, 100]
n = len(arr)
print(arr)
print("n = " + str(n) + "\n")

# calculate the variance of each unique threshold value in array (avoid iterating from 0 to 255)
arr_unique = list(set(arr))
arr_unique.sort()
print(arr_unique)

for t in arr_unique:
    try:
        print("t = " + str(t))
        # calculate the threshold value of array (0 if x <= t, 1 if x > t)
        arr_t = [(int) (x > t) for x in arr]
        print(arr_t)

        # calculate the weight of each class (sum of 0s and 1s in array divided by the length of array)
        weight_1 = sum(arr_t) / n
        weight_0 = 1 - weight_1
        print("weight0 = " + str(weight_0))
        print("weight1 = " + str(weight_1))

        # calculate the mean of each class (sum of x * 0 OR 1 divided by the sum of 0s OR 1s in array)
        # if sum is 0, variance will be infinity due to division by 0
        mean_1 = sum([x * (int) (x > t) for x in arr]) / (sum(arr_t))
        mean_0 = sum([x * (int) (x <= t) for x in arr]) / (n - sum(arr_t))
        print("mean0 = " + str(mean_0))
        print("mean1 = " + str(mean_1))

        # calculate the variance of each class (sum of (each value in array - mean of class) squared divided by the sum of 0s OR 1s in array)
        # if sum is 0, variance will be infinity due to division by 0
        variance_0 = sum([((x - mean_0) ** 2) for x in arr if x <= t]) / (n - sum(arr_t))
        variance_1 = sum([((x - mean_1) ** 2) for x in arr if x > t]) / (sum(arr_t)) 
        variance_0 = round(variance_0, 2)
        variance_1 = round(variance_1, 2)
        print("variance0 = " + str(variance_0))
        print("variance1 = " + str(variance_1))

        # sum the weight of each class multiplied by the variance of each class to get the full variance of the threshold of the array (v^2 = w0 * v0^2 + w1 * v1^2)
        variance = weight_0 * variance_0 + weight_1 * variance_1
        variance = round(variance, 2)

        print("variance of " + str(t) + " = " + str(variance))
        print()
    except:
        print("Since the mean of one of the classes is 0, the variance will be infinity due to division by 0")
        print("variance of " + str(t) + " = infinity")
        print()
        break
print("End of program")