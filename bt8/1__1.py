m,n = map(int,input().split())
ab = [[0 for j in range(n+2)] for i in range(m+2)]
for i in range(1,m+1):
    l = list(map(int,input().split()))
    for j in range(0,n):
        ab[i][j+1] = l[j]
abr = [[0 for j in range(n)] for i in range(m)]
for i in range(1,m+1):
    for j in range(1,n+1):
        dem = 0
        if ab[i][j] == 1:
            if ab[i+1][j] == 1:
                dem += 1
            if ab[i - 1][j] == 1:
                dem += 1
            if ab[i][j+1] == 1:
                dem += 1
            if ab[i][j-1] == 1:
                dem +=1
            if ab[i+1][j+1] == 1:
                dem += 1
            if ab[i - 1][j - 1] == 1:
                dem += 1
            if ab[i-1][j+1] == 1:
                dem+=1
            if ab[i+1][j-1] == 1:
                dem +=1
            print(dem, end=' ')
        elif ab[i][j] == 0:
            if ab[i+1][j] == 1:
                dem += 1
            if ab[i - 1][j] == 1:
                dem += 1
            if ab[i][j+1] == 1:
                dem += 1
            if ab[i][j-1] == 1:
                dem +=1
            if ab[i+1][j+1] == 1:
                dem += 1
            if ab[i - 1][j - 1] == 1:
                dem += 1
            if ab[i-1][j+1] == 1:
                dem+=1
            if ab[i+1][j-1] == 1:
                dem +=1
            print(dem, end= ' ')
    print()
