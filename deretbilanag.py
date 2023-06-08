bilangan = int(input("Masukkan bilangan: "))

jumlah = 0
for i in range(1, bilangan+1):
    if i % 5 == 0:
        jumlah += i

print("Jumlah sederet bilangan kelipatan 5 hingga", bilangan, "adalah", jumlah)
