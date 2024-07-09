m,n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if m > n:
    k = 0
    for i in range(0,n):
        for j in range(k + 1,m):
            if b[i] == a[j]:
                k = j
                if i == n - 1:
                    print("TRUE")
                    exit()
                break
            elif b[i] != a[j]:
                if j == m - 1:
                    print("FALSE")
                    exit()
        if k == m - 1 and b[i] != a[k] :
            print("FALSE")
            exit()
elif m < n:
    k = 0
    for i in range(0,m):
        for j in range(k + 1,n):
            if a[i] == b[j]:
                k = j
                if i == m - 1:
                    print("TRUE")
                    exit()
                break
            elif a[i] != b[j]:
                if j == n - 1:
                    print("FALSE")
                    exit()
        if k == n - 1 and a[i] != b[k] :
            print("FALSE")
            exit()

                
