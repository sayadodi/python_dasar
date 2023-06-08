nama = "Dodi Dwi Riskianto"
panggilan = "Dodi"
tahun = 12

print(nama.upper())  # Dimana ingin menampilkan huruf besar semua
print(nama.capitalize())  # Mengubah huruf kalimat pertama menjadi kapital
print(nama.title())  # Mengubah kata setiap awal kalimat menjadi kapital
print(nama.replace("Dodi", "Rehan"))
print(panggilan in nama)


# Formater

biodata = nama + f" Umur {tahun}"
print(biodata)
