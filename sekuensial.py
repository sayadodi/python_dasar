#sekuensisal adalah runtutak penyelesaian masalah secara logis

#Penjumlahan 2 bilanganan

#angka1 = int(input('Masukkan angka pertama'))
#angka2 = int(input('Masukkan angka kedua'))

#eksekusi = angka1 + angka2

#print('Hasil Dari penjumlahan tersebut adalah', str(eksekusi))

#Konversi jam
detik_awal = int(input("massukkan"))
jam = int(detik_awal/3600)
menit = int((detik_awal - (jam*3600))/60)
detik = int(detik_awal - jam*3600 - menit/60)

print(str(jam), ' jam', str(menit), ' Menit', str(detik), ' detik')