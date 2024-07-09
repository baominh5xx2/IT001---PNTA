l,m = list(map(int,input().split()))
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
for i in range(0,m):
    k = input().split()
    if 'right' in k[2]:
        if 'ambulance' in k[1]:
            a1.append(int(k[0]))
        elif 'fire' in k[0]:
            a2.append(int(k[0]))
        elif 'army' in k[1]:
            a3.append(int(k[0]))
        elif 'police' in k[1]:
            a4.append(int(k[0]))
        elif 'civilian' in k[1]:
            a5.append(int(k[0]))
    else:
        if 'ambulance' in k[1]:
            b1.append(int(k[0]))
        elif 'fire' in k[1]:
            b2.append(int(k[0]))
        elif 'army' in k[1]:
            b3.append(int(k[0]))
        elif 'police' in k[1]:
            b4.append(int(k[0]))
        elif 'civilian' in k[1]:
            b5.append(int(k[0]))
def xuly(a,l1):
    for i in range(0,len(a)):
        if a[i] > l1:
            a.remove(a[i])
    return a
l1 = l*100
a11 = xuly((a1 + a2 + a3 + a4 + a5),l1)
b11 = xuly((b1+b2+b3+b4+b5),l1)
def chuyenhang(k,l1):
    k1 = []
    sum = 0 
    dodai = len(k)
    while dodai > 0:
        if k[0] <= l1:
            sum += k[0]
            if sum < l1:
                if dodai == 1:
                    k1.append(k[0])
                k.remove(k[0])
                dodai-=1
            elif sum > l1:
                k1.append(sum - k[0])
                sum = 0
            elif sum == l1:
                k1.append(sum)
                sum = 0
                k.remove(k[0])
                dodai -=1
        else:
            k.remove(k[0])
            dodai -=1
    return len(k1)
bt = chuyenhang(b11,l1)
bp = chuyenhang(a11,l1)
if bt > bp:
    print(bt*2-1)
elif bt < bp:
    print(bp*2)
elif bt == bp:
     print(bt*2)






        

        