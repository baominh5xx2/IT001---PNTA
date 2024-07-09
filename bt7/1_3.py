n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
if n > 1:
    for i in range(1,n):
        for j in range(0,i):
            if ((a[i] % a[j] == 0) or (a[j] % a[i] == 0)):
                break
        else:
            print(a[i])
            exit()
    else:
        print(-1)
        exit()
else:
    print(-1)            