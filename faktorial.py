bilangan = int(input("Masukkan angaka faktorial anda"))

i = 1
faktor = 1

while i <= bilangan:
    faktor = faktor * i

    i += 1
print(
    str(bilangan) + " != " + str(faktor)
)  # Jikan full kiri akan menampilkan hasil terakhir
