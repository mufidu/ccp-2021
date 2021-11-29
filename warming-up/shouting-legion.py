# Apabila habis dibagi 3, maka teriak "HEYA",
# Apabila habis dibagi 5, maka teriak "HOOO",
# Apabila habis dibagi 3 dan 5, maka teriak "HEYAHOOO",

# Input Format
# Sebuah baris yang mengandung bilangan bulat positif .

# Output Format
# Cetak hasilnya berdasarkan deskripsi di atas.

N = int(input())
for i in range(1, N+1):
    if i % 3 == 0 and i % 5 == 0:
        print("HEYAHOOO", end=" ")
    elif i % 3 == 0:
        print("HEYA", end=" ")
    elif i % 5 == 0:
        print("HOOO", end="  ")
    else:
        print(i, end=" ")
