from math import sqrt

x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
N = int(input())
asteroid_bahaya = 0

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)
def is_between(x2, y2,xi,yi,x1,y1):
    return distance(x2, y2,xi,yi) + distance(xi,yi,x1,y1) == distance(x2, y2,x1,y1)

for i in range(N):
    xi,yi = map(int, input().split())
    if is_between(x2, y2,xi,yi,x1,y1):
        asteroid_bahaya += 1

print(asteroid_bahaya)
