def jumlah_total_array(array):
    add = 0
    for arr in array:
        add = add + arr
    return add
def cetak_array(array):
    print("Isi Array: ")
    print(array)


array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    array[i] = int(input(f"Masukkan input ke-{i + 1} : "))
cetak_array(array)
print(f"Jumlah total isi array adalah : {jumlah_total_array(array)}")