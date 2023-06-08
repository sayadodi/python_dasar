# Data siswa dan nilai
data_siswa = ["Siswa A", "Siswa B", "Siswa C", "Siswa D", "Siswa E"]
data_nilai = [80, 95, 70, 85, 90]

# Mencari nilai terbesar
nilai_terbesar = max(data_nilai)

# Mencari indeks siswa dengan nilai terbesar
indeks_siswa = data_nilai.index(nilai_terbesar)

# Menampilkan nama siswa dengan nilai terbesar
siswa_terbaik = data_siswa[indeks_siswa]

print("Nilai terbesar:")
print(f"Nama Siswa: {siswa_terbaik}")
print(f"Nilai: {nilai_terbesar}")
