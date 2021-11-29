# Kevin membeli sebuah novel dengan n halaman berjudul "The Saga of Saga" yang menceritakan berbagai petualangan yang dilalui sang protagonis bernama Saga. Kevin pun memutuskan untuk membaca novel tesebut setiap hari sampai ia menyelesaikan novel tersebut. Hal tersebut berarti Kevin akan membaca minimal 1 halaman setiap hari sampai novel tersebut selesai. Kevin juga tidak menyukai pecahan sehingga ia hanya akan membaca sejumlah bilangan bulat halaman setiap harinya.

# Setelah mulai membaca, Kevin ternyata sangat menyukai cerita novel tersebut sehingga Kevin ingin jumlah hari yang diperlukan untuk menyelesaikan novel tersebut selama mungkin.

# Selain itu, karena Kevin mengininkan adanya variasi, Kevin tidak mau membaca jumlah halaman yang sama dalam 2 hari berturut-turut. Sebagai contoh, Kevin bisa membaca 5 halaman hari ini, 3 halaman besok, dan 5 halaman lusa, tetapi Kevin tidak bisa membaca 5 halaman hari ini dan 5 halaman lagi besok.

# Bantu Kevin mencari berapa hari maksimal yang diperlukan untuk menyelesaikan novel "The Saga of Saga"!

# Input Format

# Input terdiri dari 1 baris, yaitu n, jumlah halaman dari novel

# Output Format

# Cetak berapa hari maksimal yang diperlukan Kevin untuk menyelesaikan novel tersebut

n = int(input())
jumlah_hari = 0
pengurang = 0

while n > 0:
    if n == 2:
        n -= 2
    elif pengurang == 1:
        pengurang = 2
        n -= 2
    else:
        pengurang = 1
        n -= 1
    jumlah_hari += 1

print(jumlah_hari)
