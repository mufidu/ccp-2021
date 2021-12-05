pintu, jenis = map(int, input().split())
list_barang = []

for i in range(jenis):
    barang = list(map(int, input().split()))
    list_barang.append(barang)

list_barang = sorted(list_barang, key=lambda x: x[1], reverse=True)

# kurangi nyawa pintu
i = 0
banyak = 0
for i in list_barang:
    for j in range(i[0]):
        if pintu >= 0:
            pintu -= i[1]
            banyak += 1
    
if pintu <= 0:
    print(banyak)
else:
    print("kaerimashou!")
