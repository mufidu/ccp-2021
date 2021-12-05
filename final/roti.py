n = int(input())
roti = list(map(int, input().split()))
rotimin = 9999999999999999

for i in roti:
    if i < rotimin:
        rotimin = i

roti.remove(rotimin)

jumlah = 0

for i in roti:
    jumlah += i

print(jumlah+1)