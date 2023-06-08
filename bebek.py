jumlah_bebek = 1000
bulan = 1

while bulan <= 10:
    bebek_lahir = jumlah_bebek
    bebek_mati = jumlah_bebek * 0.2  # 20% dari jumlah bebek

    jumlah_bebek = jumlah_bebek + bebek_lahir - bebek_mati

    bulan += 1

print("Jumlah bebek setelah 10 bulan:", int(jumlah_bebek))
