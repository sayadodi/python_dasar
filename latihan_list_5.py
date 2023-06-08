# Data string
data_string = ["apel", "jeruk", "mangga", "pisang", "durian"]

# Input data yang akan dicari
data_cari = input("Masukkan data yang ingin dicari: ")

# Mencari data dan indeksnya
if data_cari in data_string:
    indeks = data_string.index(data_cari)
    print(f"Data '{data_cari}' ditemukan pada indeks {indeks}.")
else:
    print(f"Data '{data_cari}' tidak ditemukan dalam array.")
