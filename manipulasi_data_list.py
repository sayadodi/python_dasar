# Operasi Data list

data = ["Dodi", "Dwi", "Riski"]

# Mengsmbil data list
data_0 = data[0]
print(f"Data pertama index ke 0 adalah {data_0}")

data_terakhir = data[-1]
print(f"Data terakhir adalah {data_terakhir}")

# Cara mengambil info jumlah di lis
panjang_data = len(data)
print(f"Panjang data {panjang_data}")

# Manipulasi data list

# Tambah item di list
print(f"Data sebelum di tambah {data}")
data.insert(1, "Riskianto")
print(f"Data yang sudah di tambah {data}")
data.append("Wawan")  # Data ditambahkan di akhir
print(f"data {data}")

# Menambah list dalam list
data_baru = ["Fandi", "Tegar", "Raihan"]
data.extend(data_baru)
print(f"Data gabungan {data}")

# Merubah data
data[1] = "Awan"
print(f"Data berubah{data}")

# Remove data
data.remove("Raihan")
print(f"Data remove {data}")

# Remove data belakang
data.pop()
print(f"Data terkihir hilang {data}")
