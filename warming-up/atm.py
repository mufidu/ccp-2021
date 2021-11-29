# Nanda baru saja mendapatkan gaji dari part time jobnya, ia ingin pergi ke ATM untuk menarik sejumlah uang. Dia berencana untuk menarik sejumlah N ribu rupiah. Di ATM TELYU sangat canggih karna dapat mengeluarkan berbagai pecahan uang yaitu 100 ribu, 50 ribu, 20 ribu, 10 ribu, 5 ribu, 2 ribu, dan seribu.

# Bantulah Nanda menentukan berapa lembar yang perlu dia tarik dari setiap pecahan uang agar Nanda membawa lembaran uang sesedikit mungkin.

# Input Format

# Satu angka yang menyatakan berapa ribu rupiah yang Nanda tarik.

# Output Format

# 7 angka yang di pisahkan oleh spasi yang menggambarkan berapa uang 100 ribu, 50 ribu, 20 ribu, 10 ribu, 5 ribu, 2 ribu, dan seribu yang perlu ditarik.

# Sample Input 
# 77

# Sample Output 
# 0 1 1 0 1 1 0

N = int(input())
seratus = N // 100
N = N % 100
limapuluh = N // 50
N = N % 50
duapuluh = N // 20
N = N % 20
sepuluh = N // 10
N = N % 10
lima = N // 5
N = N % 5
dua = N // 2
N = N % 2
seribu = N
print(seratus, limapuluh, duapuluh, sepuluh, lima, dua, seribu)