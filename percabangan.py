nama = input("Masukkan Nama Anda")
Nilai = int(input("Masukkan Nilai Anda"))

if Nilai <= 70:
    print("Mohon Maaf Saudara " + nama +
          f"Tidak lulus karna nilai anda {Nilai}")
else:
    print("Anda Lulus")


pt = str(input("Masukkan Nama Pt Anda"))

if len(pt) < 2:  # Len Digunakan untuk mengetahui berapa jumlah hurus yang ada di vaariable
    print("Pt Anda tidak memenuhi validasi nama pt")
else:
    print("Pt anda tervalidasi")
