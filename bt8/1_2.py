m,n = map(int,input().split())
a = []
for i in range(0,m*n):
    a.append(int(input()))
ab = [[0 for j in range(n)] for i in range(m)]
k = 0
index = abs(a.index(max(a))//n)
for i in range(0,m):
    for j in range(0,n):
        ab[i][j] = a[k]
        k += 1
for i in range(0,m):
    for j in range(0,n):
        if i != index:
            print(ab[i][j], end= ' ')
    if i != index:
        print()