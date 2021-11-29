# Input Format

# Baris input pertama adalah satu bilangan bulat T yang menunjukan berapa banyak array yang diberikan.

# Lalu setiap testcase inputannya berupa N yaitu banyak anggota bilangan pada suatu array dan inputan anggota bilangan pada suatu array. Kedua inputan tersebut dipisah oleh satu spasi.

# Output Format

# Output adalah array yang sudah terurut menurun tetapi bilangan terurut yang genap ditampilkan terlebih dahulu

T = int(input())
arr = []
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for j in range(N):
        if arr[j] % 2 == 0:
            print(arr[j], end=' ')
    for j in range(N):
        if arr[j] % 2 != 0:
            print(arr[j], end=' ')
    print()
      



