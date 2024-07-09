location = list(map(str,input().split()))
a = []
b = []
c = []
for i in range(0,len(location)):
    if int(location[i]) < 0:
        b.append(i)
        a.append((location[i]))
n = 0
m = 0
while i < len(location) and m < len(b):
    v = int(''.join(location[n:b[m]]))  
    c.append(v)
    n = b[m] + 1
    m += 1
x,y = 0,0
for j in range(0,len(c)):
    if a[j] == '-1':
        y +=c[j]
    if a[j] == '-2':
        x-=c[j]
    if a[j] == '-3':
        y-=c[j]
    if a[j] == '-4':
        x+=c[j]
if x > 0 and y > 0:
    print(str(y),'-1',str(x),'-4')
elif x > 0 and y < 0:
    print(str(-y),'-3',str(x),'-4')
elif x < 0 and y > 0:
    print(str(y),'-1',str(-x),'-2')
elif x < 0 and y < 0:
    print(str(-y),'-3',str(-x),'-2')
elif x == 0 and y < 0:
    print(str(-y) + '-3')
elif x == 0 and y > 0:
    print(str(y),'-1')
elif x < 0 and y == 0:
    print(print(str(-x),'-2'))
elif x > 0 and y == 0:
    print(print(str(x),'-4'))