data_angka = [1, 2, 7, 7, 7, 2, 2, 5, 6, 7, 8, 6]

print(f"Data angka \n{data_angka}")

# Count data
jumlah_data_2 = data_angka.count(2)
jumlah_data_7 = data_angka.count(7)

print(f"Data 2 jumlah = {jumlah_data_2}")
print(f"Data 7 jumlah = {jumlah_data_7}")

# Ambil posisi data
data = ["Dodi", "Dwi", "Riski"]

print(f"data = {data}")

index_Dodi = data.index("Dodi")
print(f"Dodi berada di index {index_Dodi}")

# Mengurutkan list
print(f"Data sebelum di urut {data_angka}")
data_angka.sort()
print(f"Data angka di urutkan {data_angka}")

# Balik list
data_angka.reverse()
print(f"Data di reverse {data_angka}")
