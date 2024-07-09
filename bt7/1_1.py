n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
dem = 0
k = min(a)
for i in range(0,n):
    if a[i] == k:
        dem +=1
print(min(a),dem)