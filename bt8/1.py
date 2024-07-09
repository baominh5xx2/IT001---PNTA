m,n = map(int,input().split())
ab = [[0 for j in range(n)] for i in range(m)]
for i in range(0,m):
    l = list(map(int,input().split()))
    for j in range(0,n):
        ab[i][j] = l[j]
abr = [[0 for j in range(n)] for i in range(m)]
for i in range(0,m):
    for j in range(0,n):
        dem = 0
        if i == 0 and j == 0:
                    if ab[i][j] == 1:
                        dem +=1
                        if ab[i][j+1] == 1:
                            dem +=1
                        if ab[i+1][j] == 1:
                            dem += 1
                        if ab[i+1][j+1] 
                    abr[i][j] = dem
        elif i == 0 and j != 0:
            if i == 0 and j == n - 1:
                if ab[i][j] == 1:
                    dem += 1
                if ab[i][j-1] == 1:
                     dem+=1
                if ab[i - 1][j] == 1:
                     dem  +=1
                abr[i][j] = dem
            elif i == 0 and j != 0 and j != n  - 1:
                if ab[i][j] == 1:
                      dem += 1
                if ab[i][j-1] == 1:
                     dem += 1
                if ab[i][j+1] == 1:
                     dem += 1
                if ab[i - 1][j] == 1:
                     dem += 1   
                abr[i][j] == dem
        elif j == 0 and i != 0:
            if i == m - 1:
                if ab[i][j] == 1:
                       dem += 1
                if ab[i][j+1] == 1:
                     dem += 1
                if ab[i - 1][j] == 1:
                     dem += 1
                abr[i][j] = dem
            elif i != m - 1:
                if ab[i][j] == 1:
                      dem += 1
                if ab[i][j+1] == 1:
                     dem += 1
                if ab[i-1][j] == 1:
                     dem += 1
                if ab[i + 1][j] == 1:
                     dem += 1
                abr[i][j] = dem
        elif i == m - 1 and j == n - 1:
                if ab[i][j] == 1:
                      dem += 1
                if ab[i][j-1] == 1:
                     dem += 1
                if ab[i-1][j] == 1:
                     dem += 1
                abr[i][j] = dem
        elif i == m - 1 and j != 0 and j != m - 1:
            if ab[i][j] == 1:
                      dem += 1
            if ab[i][j-1] == 1:
                    dem += 1
            if ab[i-1][j] == 1:
                     dem += 1
            if ab[i][j+1] == 1:
                dem+= 1
            abr[i][j] = dem
print(abr)
                      
             
            

        