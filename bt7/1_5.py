n = int(input())
a = list(map(int,input().split()))
dem = 0
soam = 0
for i in range(0,n):
    if a[i] == 0:
        dem+=1
for i in range(0,n):
    if a[i] < 0:
        soam+=1
if dem == n or (dem == n - 1 and soam == 1):
    print(0)
    exit()
tich= 1
max=-1000000000
for i in range(0,n):
    if a[i] != 0:
        tich*=a[i]
    if a[i]<0 and a[i]>max:
        max=a[i]
if tich<0:
    print(int(tich/max))
else:
    print(int(tich))