t = int(input())
a = [int(input()) for i in range(0, t)]

def xor(i, j):
    tmp = i
    for k in range(i+1, j+1):
        tmp ^= k
    return tmp

for i in a:
    if i == 1 or i == 2:
        print(1)
        print(i)
        continue
    if i == 3:
        print(2)
        print(1, 2)
        continue
    tmp = 2
    for k in range(3,i - 1):
        tmp ^= k
    #tmp = xor(2, i-2)
    tmp1 = 1^tmp^(i-1)^i
    print(tmp1)
    if tmp1 == i:
        print(i)
        for j in range(1, i+1):
            print(j, end=" ")
        print()
        continue
    tmp1 = 1^tmp^(i-1)
    tmp2 = 1^tmp^i
    if tmp1 == i:
        print(i-1)
        for j in range(1, i):
            print(j, end=' ')
        print()
        continue
    if tmp2 == i:
        print(i-1)
        for j in range(1, i-1):
            print(j, end=' ')
        print(i)
        continue
    tmp1 = tmp^(i-1)^i
    if tmp1 == i:
        print(i-1)
        for j in range(2, i+1):
            print(j, end=' ')
        print()
        continue
    tmp1 = 1^tmp
    tmp2 = tmp^(i-1)
    tmp3 = tmp^i 
    if tmp1 == i:
        print(i-2)
        for j in range(1, i-1):
            print(j, end=' ')
        print()
        continue
    if tmp2 == i:
        print(i-2)
        for j in range(2, i):
            print(j, end=' ')
        print()
        continue
    if tmp3 == i:
        print(i-2)
        for j in range(2, i-1):
            print(j, end=' ')
        print(i)
        continue
    if tmp == i:
        print(i-3)
        for j in range(2, i-1):
            print(j, end=' ')
        print()
        continue
        
        
        

        

