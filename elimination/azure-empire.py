# Anda sedang berada di kelas sejarah, dan mendengarkan cerita dari dosen anda mengenai kerajaan Azure.

# Kerajaan Azure adalah kerajaan yang sekarang sudah tidak dihuni lagi, salah satu alasannya adalah karena kerajaan tersebut memiliki N kota (yang di mana masing-masing kota memiliki nama yang unik dan berupa string), yang saling tidak terhubung, terpisahkan oleh lautan beracun, serta setiap kota memiliki kondisi udara yang berbeda-beda serta beracun. Kabarnya, untuk seseorang dapat bertahan hidup pada kerajaan Azure, orang tersebut harus tinggal di kota yang berbeda dari hari sebelumnya, yaitu tidak boleh ada 2 hari yang berurutan di mana orang tersebut tinggal di kota yang sama.

# Kabar baiknya, kerajaan tersebut meninggalkan berbagai macam teknologi, salah satunya adalah perangkat teleportasi. Dikabarkan, pada kerajaan tersebut terdapat M pasang perangkat teleportasi. Setiap perangkat teleportasi dapat digunakan untuk teleportasi ke lokasi pasangan dari perangkat teleportasi tersebut (bisa saja di kota yang sama).

# Anda pun jadi bertanya-tanya kepada diri anda sendiri. Apabila anda dipindahkan ke suatu kota pada kerajaan Azure secara acak (dengan kemungkinan terpilihnya sama untuk setiap kota), apakah anda bisa bertahan hidup? ada berapa kota yang aman untuk ditempati (yaitu yang membuat anda dapat bertahan hidup)?

# Karena anda sangat penasaran, anda pun memutuskan untuk mencari jawabannya. Oleh karena itu, bantulah diri anda dengan mencari jawabannya!

# Input Format

# Baris pertama berisikan dua bilangan, N dan M.

# M baris selanjutnya, berisikan dua string A dan B, yang berarti ada perangkat teleportasi di kota A, yang di mana pasangan dari perangkat teleportasi tersebut berada pada kota B.

# Output Format

# Keluarkan banyak kota yang aman untuk ditempati (yaitu yang membuat anda dapat bertahan hidup).

N, M = map(int, input().split())
kota_aman = set()
for i in range(M):
    A, B = input().split()
    if A != B:
        kota_aman.add(A)
        kota_aman.add(B)

print(len(kota_aman))
    
