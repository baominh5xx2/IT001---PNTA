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
n = int(input())
print(ktra(n))