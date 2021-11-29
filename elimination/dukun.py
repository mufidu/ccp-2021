# Hari ini, ia akan melayani sebanyak T pasien. Setiap pasiennya, memiliki sebuah bilangan N.

# Bila bilangan N dari pasien tadi dapat disusun ulang digit-digitnya sehingga menjadi kelipatan 25, maka pasien tersebut "Beruntung", dan sebaliknya tidak.

# Input Format

# Baris pertama, berisikan sebuah bilangan T.

# T baris berikutnya, berisikan sebuah bilangan N.

# Output Format

# Untuk setiap pasiennya, keluarkan "Beruntung" apabila pasien tersebut beruntung atau "Tidak Beruntung" apabila pasien tersebut tidak beruntung, sesuai ketentuan yang sudah dideskripsikan pada problem statement.

# Sample Input 0
# 123
# 255
# 2020

# Sample Output 0
# Beruntung
# Beruntung
# Beruntung

# Explanation 0

# Pasien ke-1 memiliki bilangan 123, dan tidak mungkin ada susunan sehingga bilangan tersebut menjadi kelipatan 25.

# Pasien ke-2 memiliki bilangan 255, dan memungkinkan untuk disusun sehingga menjadi bilangan kelipatan 25, yaitu 525.

# Pasien ke-3 memiliki bilangan 2020, dan memungkinkan untuk disusun sehingga menjadi bilangan kelipatan 25, yaitu 2200.

T = int(input())
for i in range(T):
    N = input()
    # if "25" in N or "50" in N or "75" in N or "00" in N:
    if ("2" in N and "5" in N) or ("5" in N and "0" in N) or ("7" in N and "5" in N) or ("0" in N and "0" in N):
        print("Beruntung")
    else:
        print("Tidak Beruntung")
    
