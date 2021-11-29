# Terdapat N daerah berderetan, yaitu daerah 1,2,3...N. Lalu terdapat L buah mata air, yaitu pada daerah d1,d2,...dk.

# Setiap mata air ini akan secara terus-menerus mengeluarkan air, sehingga akan menyebarkan air ke arah kanan dan kiri dengan kecepatan 1 daerah/detik.

# Pada awalnya, belum ada mata air yang mengeluarkan airnya satupun.

# Tentukan pada detik ke berapa setiap daerah mulai terkena air!

# Input Format

# Masukan terdiri dari 2 baris.

# Baris pertama, diberikan 2 bilangan bulat N dan L.

# Baris kedua, diberikan L bilangan bulat yang terpisahkan oleh spasi yaitu d1, d2,..., dk.

# Output Format

# Luaran hanya terdiri dari 1 baris, yaitu N bilangan bulat terpisah yang menandakan pada detik ke berapa tiap daerah mulai terkena air.

# Sample Input 0
# 10 2
# 2 7
# Sample Output 0
# 2 1 2 3 3 2 1 2 3 4

N, K = map(int, input().split())
L = list(map(int, input().split()))
daerah_air = []

for i in range(N):
    daerah_air.append(False)

def cek_air(daerah):
    for i in daerah:
        if daerah_air[i] == False:
            return False
    return True

detik = 0

while cek_air(daerah_air) == False:
    detik += 1
    for i in L:
        if i+detik-2 <= N and i-1-detik >= 0:
            if daerah_air[i+detik-2] == False:
                daerah_air[i+detik-2] = detik
            if daerah_air[i-1-detik] == False:
                daerah_air[i-1-detik] = detik

for i in range(N):
    print(daerah_air[i], end=" ")

        