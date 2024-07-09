m,n = map(int,input().split())
ab = [[0 for j in range(n)] for i in range(m)]
for i in range(0,m):
    l = list(map(int,input().split()))
    for j in range(0,n):
        ab[i][j] = l[j]
for i in range(m - 1,-1,-1):
    for j in range(0,n):
        print(ab[i][j], end= ' ')
    print()