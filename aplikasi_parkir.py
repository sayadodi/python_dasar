print ("============ aplikasi parkir ============")
jam_Masuk = int(input("jam berapa anda masuk tempat parkir ? : "))
jam_Keluar = int(input("jam berapa anda masuk tempat parkir ? : "))

if jam_Masuk < jam_Keluar :
    jam_Parkir = jam_Keluar-jam_Masuk
    if jam_Parkir > 2 :
        biaya = jam_Parkir-2
        biaya2 = biaya*500
        total = biaya2 + 2000
        print ("anda parkir selama " ,jam_Parkir, "jam, dan biaya parkir = " ,total)
    else :
        total = 2000
        print ("anda parkir selama " ,jam_Parkir, "jam, dan biaya parkir = " ,total)

else:
    jam_Parkir = 12-jam_Masuk+jam_Keluar
    if jam_Parkir > 2 :
        biaya = jam_Parkir-2
        biaya2 = biaya*500
        total = biaya2 + 2000
        print ("anda parkir selama " ,jam_Parkir, "jam, dan biaya parkir = " ,total)
    else :
        total = 2000
        print ("anda parkir selama " ,jam_Parkir, "jam, dan biaya parkir = " ,total) 
