mahasiswa = {}
lulus = {}

n = int(input("Masukkan banyak mahasiswa yang ingin diinput: "))
for i in range(int(n)):
    nama = str(input(f"Masukkan nama mahasiswa ke-{(i + 1)}: "))
    nilai = int(input(f"Masukkan nilai mahasiswa ke-{(i + 1)}: "))
    mahasiswa[nama] = nilai

kkm = int(input(f"Masukkan nilai KKM: "))
for idx, nama in enumerate(mahasiswa):
    if mahasiswa[nama] > kkm:
        lulus[nama] = mahasiswa[nama]
print(f"Siswa yang lulus: {sorted(lulus)}")