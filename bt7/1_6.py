n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
x = int(input())
a.sort()
#timkiemnhiphan
def binary_search(a, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
b = []
for i in range(0,n):
    k = x - a[i]
    s = binary_search(a,0,n-1,k)
    if s != -1:
        b.append(k)
        b.append(a[i])
b.sort()
if b[int(len(b)/2)-1] > b[int(len(b)/2)]:
    print(b[int(len(b)/2)])
    print(b[int(len(b)/2)-1])
else:
    print(b[int(len(b)/2)-1])
    print(b[int(len(b)/2)])