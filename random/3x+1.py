def f(x):
    i = 0
    while(x[i] != 1):
        if x[i] % 2 == 1:
            x.append((3*x[i]) + 1)
        elif x[i] % 2 == 0:
            x.append(x[i]/2)
        i += 1
    print(x)
    exit

for i in range(1, 10):
    print(f"${i} : ")
    x = [i]
    f(x)