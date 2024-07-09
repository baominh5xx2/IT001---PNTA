m = int(input())
ab = [[0 for j in range(m)] for i in range(m)]
a = []
for i in range(1,m*m+1):
    a.append(i)
i = 0
j = 0
l = 0
while i < m*m :
    for j in range(l,m - l):
        ab[l][j] = a[i] 
        i+=1
    for k in range(l + 1, m - l):
        ab[k][m - l - 1] = a[i]
        i += 1
    for j in range(m - l - 2, l - 1,-1):
        ab[m -l - 1][j] = a[i]
        i += 1
    for k in range(m - l - 2,l,-1):
        ab[k][l] = a[i]
        i+=1
    l += 1
for i in range(0,m):
    for j in range(0,m):
        print(ab[i][j], end= ' ')
    print()

