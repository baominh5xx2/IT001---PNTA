m,n = map(int,input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
abr = [[0 for j in range(n)] for i in range(m)]
l = 0
i = 0
if n > 1 and m > 1:
    while i < m*n:
        if l % 2 == 0:
            if l == m // 2 and m < n:
                    for j in range(n - l - 1,l-1,-1):
                        abr[l][j] = ab[l][j-1]
                        i += 1
                    abr[l][l] = ab[l][n-l-1]
                    i += 1
            elif l == n // 2 and m > n:
                    for j in range(l,m - l - 1):
                        abr[j][l] = ab[j+1][l]
                        i += 1
                    abr[m-l][l] = ab[l][l]
                    i += 1
            else:
                for j in range(l+1,n - l):
                    abr[l][j] = ab[l][j-1]
                    i += 1
                for k in range(l+1,m - l):
                    abr[k][n - l - 1] = ab[k-1][n - l -1]
                    i += 1
                for j in range(n - l - 2,-1+l,-1):
                    abr[m - l - 1][j] = ab[m - l - 1][j+1]
                    i += 1
                for k in range(m - l - 2,-1+l,-1):
                    abr[k][l] = ab[k + 1][l]
                    i += 1
        else:
                if l == m // 2 and m < n:
                    for j in range(l,n - l - 1):
                        abr[l][j] = ab[l][j+1]
                        i += 1
                    abr[l][n-l-1] = ab[l][l]
                    i += 1
                elif l == n // 2 and m > n:
                    for j in range(l,m - l - 1):
                        abr[j][l] = ab[j+1][l]
                        i += 1
                    abr[m-l-1][l] = ab[l][l]
                    i += 1
                else:
                    for j in range(l,n - l - 1):
                        abr[l][j] = ab[l][j+1]
                        i += 1
                    for k in range(l+1,m - l):
                        abr[k][l] = ab[k - 1][l]
                        i += 1
                    for j in range(l+1,n - l):
                        abr[m - l - 1][j] = ab[m - l - 1][j-1]
                        i += 1
                    for k in range(m - l - 2,l-1,-1):
                        abr[k][n - l - 1] = ab[k+1][n - l -1]
                        i += 1  
        l += 1
        if m*n % 2 != 0 and i == m*n - 1:
            abr[m//2][n//2] = ab[m//2][n//2]
            i += 1
    for i in range(0,m):
        for j in range(0,n):
            print(abr[i][j], end= ' ')
        print()
elif n == 1 and m > 1:
        print(ab[m-1][0])
        for i in range(0,m-1):
            print(ab[i][0])
elif m == 1 and n > 1:
        abr[0][0] = ab[0][n-1]
        for i in range(0,n):
            abr[0][i] = ab[0][i-1]
        for j in range(0,n):
                print(abr[0][j], end= ' ')
elif m == 1 and n == 1:
    print(ab[0][0])



