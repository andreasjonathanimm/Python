import sys
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
B = [2, 1, 0, 5, 3, 4, 9, 7, 8, 6]
C = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def findNum(arr):
    i = []
    for idx, n in enumerate(arr):
        i.append(idx)
        if 9 == n:
            print(i)
            return True
    print(i)
    return False

print(findNum(A))
print(findNum(B))
print(findNum(C))