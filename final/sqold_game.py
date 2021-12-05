N, M, A, B = map(int, input().split())
list_pemain = []

for i in range(N):
    we = list(map(int, input().split()))
    list_pemain.append(we)

for i in list_pemain:
    w, e = i[0], i[1]
    i.append(w*A+e*B)

list_pemain = sorted(list_pemain, key=lambda x: x[2], reverse=True)

list_pemain = list_pemain[:M]

poin_tim = 0

for i in list_pemain:
    poin_tim += i[2]

print(poin_tim)