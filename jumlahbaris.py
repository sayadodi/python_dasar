jml_baris_kolom = int(input("Masukkan jumlah baris dan kolom "))
i = 1

while i <= jml_baris_kolom:
    hasil = ""
    j = 1
    while j <= jml_baris_kolom:
        hasil = hasil + str(i) + ""
        j += 1
    print(hasil)
    i += 1
