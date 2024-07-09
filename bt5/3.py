x,y = map(int,input().split())
def ucln(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b-=a
    return a
bcnn = int((x*y)/ucln(x,y))
for i in range(1,1000000000):
    a = i
    b = a + bcnn
    c = b + bcnn
    d = c + bcnn
    if(a+b)%x == 0 and (a+c)%x == 0 and (a+d)%x == 0 and (b+c)%x == 0 and (b+d)%x==0 and (c+d)%x==0 and (a+b+c)%y==0 and (a+b+d)%y==0 and(a+c+d)%y==0 and(b+c+d)%y==0:
        print(a+b+c+d)
        exit()