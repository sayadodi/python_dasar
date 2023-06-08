secret = 5
mulai = 1
batas = 3
print("Tebaklah angka 1-10 dibawah ini")

guessed_correctly = False  # Pembacaan buat validasi

while mulai <= batas:
    user = int(input(f"Masukkan tebakan anda yang ke-{mulai}: "))

    if user == secret:
        print(f"Selamat, tebakan anda benar pada tebakan ke-{mulai}!")
        guessed_correctly = True
        break

    mulai += 1

if not guessed_correctly:
    print("Kesempatan anda hangus")
