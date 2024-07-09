import math
def snt(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(3,int(math.sqrt(n))):
        if n % i == 0:
            return False
    else:
        return True
import gmpy2
def snt1(n):
    if n <= 1:
        return False
    return gmpy2.is_prime(n)
def gido(n):
    a = []
    bandau = 2
    while n > 1:
        while n % bandau == 0 and snt1(bandau) == True:
            a.append(bandau)
            n //= bandau
        bandau += 1
    return a
n = int(input())
k = gido(n)
i = 0
print(len(set(k)))
while i < len(k):
    if k.count(k[i]) > 1:
        print(k[i],k.count(k[i]))
        i += k.count(k[i])
    else:
        print(k[i],k.count(k[i]))
        i += 1

