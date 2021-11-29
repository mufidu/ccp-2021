# Pada soal ini kalian hanya diminta untuk menjumlahkan dua bilangan pecahan  dan  dengan presisi .

# Catatan: jika bilangan di belakang bilangan terakhir lebih dari sama dengan 5, maka bilangan tersebut dibulatkan ke atas

# Input Format

# Baris pertama terdiri dari N sebuah bilangan yaitu  yang mewakili jumlah kasus. Baris-baris selanjutnya terdiri dari tiga buah bilangan yaitu X,Y, dan P yang masing-masing mewakili bilangan pertama, bilangan kedua, dan presisi. X dan Y merupakan bilangan pecahan 1-1000000, namun P adalah bilangan bulat 1-10.

# Output Format

# Keluaran adalah  baris, yang masing-masing baris adalah jawaban untuk setiap kasus.

# Sample Input 0
# 1
# 0.9579944239226834 -0.970266528964917 8

# Sample Output 0
# -0.01227211

# Sample Input 1
# 4
# -0.6502252550964456 -0.4215387027568145 6
# 6.388762779166257 9.94099282241556 4
# -47.67519502657409 27.634358782594063 4
# 926.0409988845299 125.56222615898355 3

# Sample Output 1
# -1.071764
# 16.3298
# -20.0408
# 1051.603

N = int(input())
for i in range(N):
    X, Y, P = input().split()
    X = float(X)
    Y = float(Y)
    P = int(P)
    print(round(X + Y, P - 1))
