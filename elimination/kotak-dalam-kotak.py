# Lilas memiliki n buah rubik dengan ukuran panjang dan lebar masing-masing 1 satuan dan ia ingin membeli sebuah kotak berbentuk persegi panjang yang dapat menampung seluruh rubiknya. Dalam menentukan kotak mana yang akan dibeli, Lilas memiliki 2 syarat yaitu :

# 1. Kotak tersebut harus tepat dapat menampung seluruh rubik yang dimiliki Lilas
# 2. Lilas ingin perbedaan panjang dan lebar kotak tersebut seminimal mungkin

# Bantulah Lilas menentukan berapa satuan panjang dan lebar kotak yang harus dibeli!

# Input Format

# Input terdiri dari 1 baris, yaitu , jumlah rubik yang dimiliki Lilas

# Output Format

# Cetak panjang dan lebar dari kotak yang harus dibeli secara terurut menaik.

# n = int(input())
# a, b, i = 1, n, 0
# while a < b:
#     i += 1
#     if n % i == 0:
#         a = i
#         b = n//a

n = int(input())
x = 1
y = n
i = 0
while x < y:
    i += 1
    if n % i == 0:
        x = i
        y = n//x
print(y, x)