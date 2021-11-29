# Pada permasalahan ini tugas Anda adalah menghitung nilai ke- dari sebuah deret Fibonacci dengan kondisi awal tertentu (belum tentu F0 = 0 dan F1 = 1).

# Input terdiri atas dua baris, baris pertama terdiri atas dua buah bilangan bulat F0 dan F1 yang menyatakan kondisi awal (benih) dari deret Fibonacci. Baris kedua adalah bilangan bulat non-negatif.

# Outputnya adalah sebuah bilangan bulat yang menyatakan nilai ke-n dari deret Fibonacci, yaitu Fn,dengan kondisi awal F0 and F1 dideskripsikan pada input.

# Sample Input 1
# -3 -4
# 20

# Sample Output 1
# -39603

# Sample Input 2
# 5 -3
# 30

# Sample Output 2
# 75025

F0, F1 = map(int, input().split())
N = int(input())

def fibo(n):
    if n == 0:
        return F0
    elif n == 1:
        return F1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(N))