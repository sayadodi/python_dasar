#Diractory
namaBarang = {
    "a": 2000, 
    "b": 3000, 
    "c": 4000
    }
user = int(input("Input"))
i = 1
jumlah = 0
valid = False
while i <= user:
    kode = input(f"Masukkan barang ke {i}")
    if kode in namaBarang:
        satuan = int(input("Jumlah barang yang akan di beli"))
        jumlah += namaBarang[kode] * satuan
        valid = True
    else:
        print("Pembelian gagal kerana kode yang anda masukkan tidak valid")
        valid = False
        break
    i += 1

if valid == True:
    print(jumlah)
