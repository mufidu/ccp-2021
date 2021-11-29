# Megumin adalah penyihir terkenal di kotanya dengan sihir ledakannya. Pada suatu hari, Megumin menemukan pola aneh pada tanah yang berbentuk mirip jam pasir. Namun uniknya, ketinggian jam pasir selalu ganjil dan tidak mungkin genap. Setelah melihat hal tersebut, dia menjadi penasaran bentuk dari jam tersebut dengan ketinggian n akan seperti apa bantuknya. Bantulah Megumin menemukan pola dari jam pasir tersebut.

# Input Format

# 1 baris bilangan ganjil n

# Output Format

# Print pola jam pasir Megumin dari kumpulan karakter '*'.

# Sample Input 0
# 7

# Sample Output 0
# * * * * * * * 
#   *       *   
#     *   *     
#       *       
#     *   *     
#   *       *   
# * * * * * * *

# Sample Input 1
# 5

# Sample Output 1
# * * * * * 
#   *   *   
#     *
#   *   *
# * * * * *

n = int(input())
for i in range(n):
    for j in range(n):
        if i == j:
            print('*', end=" ")
        elif i == 0 or i == n-1:
            print('*', end=" ")
        elif i == j or i == n-1-j:
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print()