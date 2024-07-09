n = int(input())
def ktra(t):
    dem = 0
    for i in range(1,):
        if(t % i == 0):
            dem+=1
    if(dem == 2):
        return 1
    else:
        return 0
count = 0
a = 1
for a in range(0,int(n/2+1)):
    if(ktra(a)==1):
        b = n - a
        if(ktra(b)==1):
            count+=1
print(count)

