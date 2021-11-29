# Andi memulai menggunakan pendeteksi kebohongan untuk mendeteksi apakah kesaksian saksi mata itu benar. Namun, Andi mengetahui bahwa pendeteksi kebohongan yang dia pakai telah rusak, sehingga ia menggunakan pendeteksi kebohongan kedua untuk mendeteksi apakah hasil dari pendeteksi kebohongan pertama adalah benar. Situasi ini terjadi berulang kali sehingga Andi akhirnya menggunakan N pendeteksi kebohongan secara total. Pendeteksi kebohongan ke-i melaporkan kebenaran dari pendeteksi kebohongan ke-i-1 untuk 1..N, dan pendeteksi kebohongan ke-1 melaporkan kebenaran kesaksian saksi mata.

N = int(input())
lie_counts = 0

for i in range(N):
    detector = input()
    if detector == "LIE":
        lie_counts += 1
    elif detector == "TRUTH":
        continue

if lie_counts % 2 == 0:
    print("TRUTH")
else:
    print("LIE")