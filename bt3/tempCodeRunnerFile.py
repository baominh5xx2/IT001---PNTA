n = int(input())
k = 5
import random
 
def snt(n, k):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
 
    r, m = 0, n - 1
    while m % 2 == 0:
        r += 1
        m //= 2
 
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, m, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
 
    return True
s = []
dem = 0
for i in range(n,0,-1):
    if snt(i,k) == True:
        dem+=1
        s.append(i)
    if dem == 3:
        print(s[1])
        exit()