import math
n = 10000000
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
count = 0
a = 1
k = int(n/100000000000)    
for a in range(k,int(n/2)+1):
    if(ktra(a)==True):
        b = n - a
        if(ktra(b)==True):
            count+=1
print(count)
