import string


import math
n = int(input())

for i in range(n):
    stringnya = input()
    huruf_sama = []
    for i in range(len(stringnya)):
        huruf_sama.append(0)
        for j in range(len(stringnya)):
            if stringnya[i] == stringnya[j] and i != j:
                huruf_sama[i] += 1
    
    bawah = 1
    print(huruf_sama)
    for i in huruf_sama:
        bawah *= math.factorial(i)

    power = math.factorial(len(stringnya))/bawah
    print(power, bawah)