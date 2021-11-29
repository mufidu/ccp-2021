# Wahid memiliki 2 kantong bola A dan B.
# Di A ada n bola dan di B ada m bola.

# Wahid mengelompokkan bola dari 2 kantong tersebut berdasarkan ukurannya, namun ia penasaran mengenai jumlah Bola Kasihan yang ada. Bola Kasihan didefinisikan sebagai bola yang berada pada kelompok yang terdiri dari bola kantong A saja atau terdiri dari bola kantong B saja.

# Bantulah Wahid menghitung jumlah Bola Kasihan!

# Input Format

# Baris pertama input terdiri dari bilangan bulat n dan m

# Baris kedua terdiri dari n bilangan bulat  dipisahkan spasi, elemen dari kantong A

# Baris ketiga terdiri dari m bilangan bulat  dipisahkan spasi, elemen dari kantong B

# Sample Input 0
# 4 3
# 1 1 5 4
# 2 1 4
# Sample Output 0
# 2

# Explanation 
# Pada kasus pertama, terdapat 4 kelompok yang dapat dibentuk yaitu untuk bola-bola berukuran :
# 1 : Terdapat 2 bola dari kantong A dan 1 dari kantong B
# 2 : Terdapat 1 bola dari kantong B
# 4 : Terdapat 1 bola dari kantong A dan 1 dari kantong B
# 5: Terdapat 1 bola dari kantong A
# Kelompok bola-bola berukuran 1 dan 4 memiliki bola dari kantong A dan kantong B sehingga tidak termasuk Bola Kasihan.
# Kelompok bola-bola berukuran 5 dan 2 merupakan Bola Kasihan sehingga output jumlah Bola Kasihan adalah 2.

# Sample Input 1
# 5 5
# 1 2 3 4 5
# 6 7 8 9 10
# Sample Output 110
# Explanation 1
# Pada kasus kedua, semua bola pada kantong A tidak akan sekelompok dengan bola dari kantong B sehingga semua bola adalah Bola Kasihan.

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# bola_kasihan = 0
# checker = False

# for i in range(n):
#     for j in range(m):
#         if a[i] == b[j]:
#             checker = True
#             break
#     if checker == False:
#         bola_kasihan += 1
#     checker = False

# for i in range(m):
#     for j in range(n):
#         if b[i] == a[j]:
#             checker = True
#             break
#     if checker == False:
#         bola_kasihan += 1
#     checker = False

# print(bola_kasihan)

# Try faster solution

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
bola_kasihan = 0
checker = False

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            checker = True
    if checker == False:
        bola_kasihan += 1
    checker = False

print(bola_kasihan)