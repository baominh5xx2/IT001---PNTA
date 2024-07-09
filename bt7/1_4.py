n = int(input())
a = list(map(int,input().split()))
k = []
for i in range(0,n):
    sum = 1
    for j in range(0,n):
        if j != i:
            sum = sum*a[j]
    k.append(sum)
print(k)