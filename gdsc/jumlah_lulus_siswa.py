# Asumsi bahwa data nilai mahasiswa dimasukkan dalam database dan dihubungkan dengan program python ini
# Program ini masih belum dibersihkan atau disingkat
# Sample dari dataNilai.csv:
a0 = b0 = c0 = d0 = a1 = b1 = c1 = d1 = a2 = b2 = c2 = d2 = lulus = 0
n_a0 = n_a1 = n_a2 = n_b0 = n_b1 = n_b2 = n_c0 = n_c1 = n_c2 = n_d0 = n_d1 = n_d2 = 0

# Misalnya nilai tiap kode siswa
siswa_nilai = {
    "10-A-1":73,
    "10-A-2":65,
    "10-A-3":40,
    "10-A-4":74,
    "10-B-40":73,
    "10-B-41":45,
    "10-C-84":90,
    "10-C-86":84,
    "10-A-120":93,
    "11-A-121":97,
    "11-A-122":59,
    "11-A-123":45,
    "11-A-124":49,
    "11-A-142":101,
    "11-B-167":100,
    "11-B-169":100,
    "11-C-200":59,
    "11-C-201":66,
    "11-D-240":58,
    "11-D-241":42,
    "11-D-242":42,
    "11-A-276":64,
    "11-A-277":81,
    "12-A-282":45,
    "12-A-285":92,
    "12-B-314":76,
    "12-B-315":84,
    "12-C-354":101,
    "12-C-355":88,
    "12-C-353":87,
    "11-C-234":78,
    "10-C-81":50
}

# Memasukkan data nilai dan jumlah setiap kelas 10, 11, dan 12, termasuk huruf A, B, C, D.
for i, kode in enumerate(siswa_nilai):
    kode1 = kode.replace("-", " ")
    siswa = kode1.split()
    if siswa[0] == '10':
        if siswa[1] == 'A':
            a0 += siswa_nilai[kode]
            n_a0+=1
        elif siswa[1] == 'B':
            b0 += siswa_nilai[kode]
            n_b0 += 1
        elif siswa[1] == 'C':
            c0 += siswa_nilai[kode]
            n_c0 += 1
        elif siswa[1] == 'D':
            d0 += siswa_nilai[kode]
            n_d0 += 1
    elif siswa[0] == '11':
        if siswa[1] == 'A':
            a1 += siswa_nilai[kode]
            n_a1+=1
        elif siswa[1] == 'B':
            b1 += siswa_nilai[kode]
            n_b1 += 1
        elif siswa[1] == 'C':
            c1 += siswa_nilai[kode]
            n_c1 += 1
        elif siswa[1] == 'D':
            d1 += siswa_nilai[kode]
            n_d1 += 1
    elif siswa[0] == '12':
        if siswa[1] == 'A':
            a2 += siswa_nilai[kode]
            n_a2+=1
        elif siswa[1] == 'B':
            b2 += siswa_nilai[kode]
            n_b2 += 1
        elif siswa[1] == 'C':
            c2 += siswa_nilai[kode]
            n_c2 += 1
        elif siswa[1] == 'D':
            d2 += siswa_nilai[kode]
            n_d2 += 1

# Belum menemukan cara untuk menghilangkan variabel nol atau kosong
if n_d0 == 0: n_d0 = 1
if n_d1 == 0: n_d1 = 1
if n_d2 == 0: n_d2 = 1

# Menghitung rata-rata nilai setiap kelas
rata_rata_a0 = a0/n_a0
rata_rata_a1 = a1/n_a1
rata_rata_a2 = a2/n_a2
rata_rata_b0 = b0/n_b0
rata_rata_b1 = b1/n_b1
rata_rata_b2 = b2/n_b2
rata_rata_c0 = c0/n_c0
rata_rata_c1 = c1/n_c1
rata_rata_c2 = c2/n_c2
rata_rata_d0 = d0/n_d0
rata_rata_d1 = d1/n_d1
rata_rata_d2 = d2/n_d2

# Menghitung banyak siswa yang lulus dengan memperhitungkan seluruh nilai siswa yang melebihi rata-rata kelas
for i, kode in enumerate(siswa_nilai):
    kode1 = kode.replace("-", " ")
    siswa = kode1.split()
    if siswa[0] == '10':
        if (siswa[1] == 'A' and siswa_nilai[kode] > rata_rata_a0) or (siswa[1] == 'B' and siswa_nilai[kode] > rata_rata_b0) or (siswa[1] == 'C' and siswa_nilai[kode] > rata_rata_c0) or (siswa[1] == 'D' and siswa_nilai[kode] > rata_rata_d0):
            lulus += 1
    elif siswa[0] == '11':
        if (siswa[1] == 'A' and siswa_nilai[kode] > rata_rata_a1) or (siswa[1] == 'B' and siswa_nilai[kode] > rata_rata_b1) or (siswa[1] == 'C' and siswa_nilai[kode] > rata_rata_c1) or (siswa[1] == 'D' and siswa_nilai[kode] > rata_rata_d1):
            lulus += 1
    elif siswa[0] == '12':
        if (siswa[1] == 'A' and siswa_nilai[kode] > rata_rata_a2) or (siswa[1] == 'B' and siswa_nilai[kode] > rata_rata_b2) or (siswa[1] == 'C' and siswa_nilai[kode] > rata_rata_c2) or (siswa[1] == 'D' and siswa_nilai[kode] > rata_rata_d2):
            lulus += 1
print(lulus)