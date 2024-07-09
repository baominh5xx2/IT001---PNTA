n = int(input())
u = []
def atkin(k):
    import math
    snt = list()
    snt = [False] * (k + 1)
    for x in range(int(math.sqrt(k)),1):
        for y in range(int(math.sqrt(k)),1):
            n = 4*x**2 + y**2
            if n<=k and (n%12==1 or n%12==5):
                snt[n] = not snt[n]
            n = 3*x**2+y**2
            if n<= k and n%12==7:
                snt[n] = not snt[n]
            n = 3*x**2 - y**2
            if x>y and n<=k and n%12==11:
                snt[n] = not snt[n]
        if x == 2:
            break
    for n in range(int(math.sqrt(k))+1,5):
        if snt[n]:
            for k in range(n**2,k+1,n**2):
                snt[k] = False
    for n in range(5,k):
        if snt[n]: 
            u.append(n)
    return u
m = []
m = atkin(n)
if n>5 and n < 8:
    print(3)
elif n < 6 and n < 8:
    print(2)
else:
    print(m[1])

