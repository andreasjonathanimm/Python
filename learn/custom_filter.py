vals = [-1, 2, 0, 11, 9, -3, -4, 3]
positive = []
for val in vals:
    if val > 0:
        positive.append(val)
print(sorted(positive))