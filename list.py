## --- LIST --- ##

# Kumpulan Data Numbers
data_siswa = [1, 2, 3]
print(data_siswa)

# Kumpulan Data String
data_siswa = ["Dodi", "Dwi", "Riski"]
print(data_siswa)

# Kumpulan Data Bolean
data_siswa = [True, False, True]
print(data_siswa)

# Alternatif membuat list
data_range = range(0, 10, 1)  # Range(Start, Stop, Step)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop
list_dengan_for = [i**2 for i in range(1, 10)]
print(list_dengan_for)

# Membuat list pake for if
list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)
