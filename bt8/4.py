m, n = map(int, input().split())
image = [input() for _ in range(m)]
ab = [[0 for j in range(n+2)] for i in range(m+2)]
for i in range(1,m+1):
        k = list(image[i-1])
        for l in range(1,n+1):
            if '-' in k[l-1]:
                ab[i][l] = 1
for o in ab:
     print(o)
case = 0
for i in range(0,m):
    for j in range(0,n):
        if ab[i+1][j] == 1 and ab[i][j] == 1 and ab[i - 1][j] == 1:
             print(i+1,j+1)
            
                
                 
                
                

    
    