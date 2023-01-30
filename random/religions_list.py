from typing import Counter


religions = ["Islam", "Buddha", "Katolik", "Kristen Protestan", "Konghucu", "Hindu"]
print('Macam-Macam Agama di Indonesia : ')
count = 1
for religion in religions:
    print(str(count) + ". " + religion)
    count+=1