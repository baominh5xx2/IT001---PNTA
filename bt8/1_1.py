r,c = map(int,input().split())
ab = [[0 for j in range(c)] for i in range(r)]
a = []
for i in range(0,r):
    l = list(map(int,input().split()))
    for j in range(0,c):
        ab[i][j] = l[j]
for i in range(r-1,-1,-1):
    for j in range(c-1,-1,-1):
        print(ab[i][j], end= ' ')
    print()