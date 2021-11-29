# Input Format

# Baris 1 terdiri dari n orang raksasa.

# Baris selanjutnya terdiri dari n buah bilangan yang menyatakan ukuran raksasa.

# Output Format

# Keluarkan ukuran raksasa terkecil ke-3 jika terdapat raksasa dengan ukuran terkecil ke-3. Jika tidak ada, keluarkan "sasageo" tanpa tanda petik.

# PERHATIKAN : terkecil 1 HARUS tidak sama dengan terkecil 2
# Syarat raksasa dikatakan terkecil ke 3 ketika raksasa terkecil 1 atau 2 tidak sama dengan yang ke 3. Jika tidak ada raksasa dengan ukuran terkecil ke 3, keluarkan "sasageo".

# Sample Input 0
# 7
# 5 4 8 3 5 6 4
# Sample Output 0
# 5

# Sample Input 1
# 3
# 2 1 2
# Sample Output 1
# sasageo

n = int(input())
arr = list(map(int, input().split()))
kecil1 = kecil2 = kecil3 = 99999999999999999999999

for i in arr:
    if i < kecil1:
        kecil1 = i
for i in arr:
    if i < kecil2 and i != kecil1:
        kecil2 = i
for i in arr:
    if i < kecil3 and i != kecil1 and i != kecil2:
        kecil3 = i
if kecil3 == 99999999999999999999999:
    print("sasageo")
else:
    print(kecil3)