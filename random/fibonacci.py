def fibonacci(x):
    if x < 0:
        print("Wrong number")
        exit()
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
n = int(input("Enter a number: "))
print(fibonacci(n))
