import sys
f = sys.stdin.readline
INF =int(1e9)

n = int(f()) #도시의 개수 입력
m = int(f()) #버스의 개수 입력
cities = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            cities[a][b] = 0

#간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, f().split())
    cities[a][b] = min(cities[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cities[a][b] = min(cities[a][b], cities[a][k]+cities[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if cities[a][b] == INF:
            print(0, end=" ")
        else:
            print(cities[a][b], end=" ")
    print()