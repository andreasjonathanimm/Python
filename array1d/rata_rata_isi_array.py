def rata_rata(array):
    add = 0
    for arr in array:
        add = add + arr
    return add/len(array)

def cetak_array(array):
    print("Isi array: ")
    print(array)

n = int(input("Masukkan banyak data array : "))
array = [None] * n
for idx, num in enumerate(array):
    array[idx] = int(input(f"Masukkan isi array ke-{idx+1} : "))
cetak_array(array)
print(f"Rata-rata : {rata_rata(array)}")