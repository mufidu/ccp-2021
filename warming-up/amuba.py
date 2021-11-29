# Ia memulai bisnisnya dengan N amuba. Jenis amuba yang ia kembang biakkan akan melahirkan 1 amuba baru setiap menitnya setelah mereka berumur X menit.

# Bantulah Wisnu memprediksi berapa banyak amuba yang ia miliki setelah T menit!

# Input Format

# Input terdiri dari 3 bilangan : N, X, T

# Output Format

# Keluaran berupa 1 bilangan bulat, banyaknya amuba yang dimiliki Wisnu setelah T menit (dalam modulo 1000000007).

N, X, T = input().split()

for i in range(int(T)):
    N = (N * int(X)) % 1000000007
    
