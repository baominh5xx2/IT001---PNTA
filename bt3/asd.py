n = int(input())
import math
def ktra(t):
    if t <= 1:
        return False
    if t == 2:
        return True
    if t % 2 == 0:
        return False
    for d in range(3, math.isqrt(t) + 1, 2):
        if t % d == 0:
            return False
    else:
        return True
s = []
dem = 0
for i in range(n,0,-1):
    if ktra(i) == True:
        dem+=1
        s.append(i)
    if dem == 3:
        print(s[1])
        exit()