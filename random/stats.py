from cmath import sqrt
from statistics import median

tot = 0
nilai = [79, 79, 48, 74, 81, 98, 87, 80, 80, 84, 90, 70, 91, 93, 82, 78, 70, 71, 92, 38, 56, 81, 74, 73, 68, 72, 85, 51, 65, 93, 83, 86, 90, 35, 83, 73, 74, 43, 86, 88, 92, 93, 76, 71, 90, 72, 67, 75, 80, 91, 61, 72, 97, 91, 88, 81, 70, 74, 99, 95, 80, 59, 71, 77, 63, 60, 83, 82, 60, 67, 89, 63, 76, 63, 88, 70, 66, 67, 79, 75]
nilai = sorted(nilai)
med = median(nilai)
avg = sum(nilai)/len(nilai)
for i in nilai:
    tot += pow((i - avg), 2)
s = sqrt(tot/len(nilai))
print(s)