m,n = map(int,input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
c = []
for i, m in enumerate(ab[1:-1],1):
    for j, n in enumerate(m[1:-1],1):
        tong = 0
        tong = (ab[i][j] + ab[i-1][j-1] + ab[i-1][j] + ab[i - 1][j+1] +ab[i][j+1] + ab[i+1][j+1] + ab[i+1][j] + ab[i][j-1] + ab[i+1][j-1])//9
        c.append(tong)
    print(''.join(map(str,c)))