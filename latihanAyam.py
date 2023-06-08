golongan = int(input("Masukkan golongan anda "))
jamKerja = float(input("Masukkan jam kerja "))

NormalGaji = 0
lembur = 0
satuanJam = 0

if golongan == 1:
    satuanJam = 3000
elif golongan == 2:
    satuanJam = 3500
elif golongan == 3:
    satuanJam = 4000
elif golongan == 4:
    satuanJam = 5000
else:
    print("Maaf golongan anda tidak ditemukan")
    exit

if jamKerja > 40:
    NormalGaji = satuanJam * jamKerja
    lembur = (satuanJam * 0.5) * (jamKerja - 40)
else:
    NormalGaji = satuanJam * jamKerja

totalGaji = NormalGaji + lembur

print(f"Total gaji anda adalah = {totalGaji}")
