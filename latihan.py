# Input jam masuk dan jam keluar
jam_masuk = int(input("Masukkan jam masuk (1-12): "))
jam_keluar = int(input("Masukkan jam keluar (1-12): "))

# Perhitungan lama parkir
if jam_keluar < jam_masuk:
    jam_keluar += 12
    lama_parkir = jam_keluar - jam_masuk
else:
    lama_parkir = jam_keluar - jam_masuk


# Perhitungan biaya parkir
print(lama_parkir)
