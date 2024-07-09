m,n = map(int,input().split())
ab = [[0 for j in range(n+2)] for i in range(m+2)]
for i in range(1,m+1):
    k = list(map(int,input().split()))
    for j in range(1,n+1):
        ab[i][j] = k[j-1]
dem = 0
for i in range(1,m+1):
    for j in range(1,n+1):
        if ab[i][j] == 1:
            if ab[i+1][j] == 0:
                dem += 1
            if ab[i-1][j] == 0:
                dem += 1
            if ab[i][j+1] == 0:
                dem += 1
            if ab[i][j-1] == 0:
                dem += 1
print(dem)