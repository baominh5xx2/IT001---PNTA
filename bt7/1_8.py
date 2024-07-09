n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
for i in range(0,n):
    if a[i] == 1:
        print(1)
        print(1)
        continue
    if a[i] == 2:
        print(1)
        print(2)
        continue
    if a[i] == 3:
        print(2)
        print(1,2)
        continue
    target = 2
    for j in range(3,a[i] - 1):
        target ^= j
    target1 = 1^target^(a[i]-1)^a[i]
    if target1 == a[i]:
        print(a[i])
        for j in range(1, a[i]+1):
            print(j,end =' ')
        print()
        continue
    target1 = 1^target^(a[i]-1)
    target2 = 1^target^a[i]
    if target1 == a[i]:
        print(a[i] - 1)
        for j in range(1, a[i]):
            print(j,end=' ')
        print()
        continue
    if target2 == a[i]:
        print(a[i] - 1)
        for j in range(1, a[i]-1):
            print(j, end=' ')
        print(a[i])
        continue
    target1 = target^(a[i]-1)^a[i]
    if target1 == a[i]:
        print(a[i]-1)
        for j in range(2, a[i]+1):
            print(j,end=' ')
        print()
        continue
'''    target1 = 1^target
    target2 = target^(a[i]-1)
    target3 = target^a[i]
    if target1 == a[i]:
        print(a[i]-2)
        for j in range(1, a[i] - 1):
            print(j,end=' ')
        print()
        continue
    if target2 == a[i]:
        print(a[i]-2)
        for j in range(2, a[i]):
            print(j,end=' ')
        print()
        continue
    if target3 == a[i]:
        print(a[i] - 2)
        for j in range(2, a[i] - 1):
            print(j,end=' ')
        print(a[i])
        continue
    if target == a[i]:
        print(a[i]-3)
        for j in range(2, a[i]  - 1):
            print(j,end=' ')
        print()
        continue'''



