batas = int(input("Masukkan batas: "))

prev1 = 1
prev2 = 1

print(prev1, prev2, end=" ")

while prev2 <= batas:
    next_number = prev1 + prev2
    if next_number <= batas:
        print(next_number, end=" ")
    prev1, prev2 = prev2, next_number
