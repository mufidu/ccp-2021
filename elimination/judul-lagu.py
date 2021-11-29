# Input Format

# Input terdiri dari banyak baris dengan ketentuan sebagai berikut :

# Baris pertama berisi sebuah bilangan bulat N yang menyatakan banyaknya lagu.

# Baris kedua berisi durasi video dalam format hh:mm:ss.

# Baris ketiga berisi waktu ketika Alex mendengarkan lagu tersebut dalam format hh:mm:ss.

# Untuk hh:mm:ss baris berikutnya berisi nama lagu dan kapan lagu tersebut di putar dalam format N yang dipisahkan dengan tanda "-".

# Output Format

# Output terdiri dari satu baris yang berisi nama lagu yang ingin dicari Alex.

N = int(input())
hhv, mmv, ssv = map(int, input().split(':'))
durasi_video = hhv * 3600 + mmv * 60 + ssv
hhl, mml, ssl = map(int, input().split(':'))
durasi_lagu = hhl * 3600 + mml * 60 + ssl
list_lagu = []

for i in range(N):
    lagu, durasi = input().split('-')
    hh, mm, ss = map(int, durasi.split(':'))
    durasi_lagulagu = hh * 3600 + mm * 60 + ss
    list_lagu.append(lagu + '-' + str(durasi_lagulagu))

list_lagu.append(f"Video - {durasi_video}")

for i in range(N-1):
    lagu1, durasi1 = list_lagu[i].split('-')
    lagu2, durasi2 = list_lagu[i+1].split('-')
    durasi_lagu1 = int(durasi1)
    durasi_lagu2 = int(durasi2)

    if durasi_lagu > durasi_lagu1 and durasi_lagu < durasi_lagu2:
        print(lagu1)
        break

    elif durasi_lagu == durasi_lagu1:
        print(lagu1)
        break

    elif durasi_lagu == durasi_lagu2:
        print(lagu2)
        break
    