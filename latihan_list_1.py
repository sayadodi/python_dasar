# Data siswa dan frekuensi kehadiran
data_siswa = ["Siswa A", "Siswa B", "Siswa C", "Siswa D", "Siswa E"]
frekuensi_kehadiran = [15, 12, 17, 10, 13]

# Mencari frekuensi kehadiran maksimum
max_frekuensi = max(frekuensi_kehadiran)

# Menampilkan grafik bintang
for i in range(len(data_siswa)):
    bar = "*" * frekuensi_kehadiran[i]
    print(f"{data_siswa[i]}: {bar} ({frekuensi_kehadiran[i]})")

    # Menambahkan garis horizontal untuk memperjelas grafik
    print("-" * max_frekuensi)
