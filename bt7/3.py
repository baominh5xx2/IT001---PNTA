x = int(input())
a = []
check = True
while check:
    a = list(map(int, input().split()))
    for j in a:
        if j == -1:
            check = False
            a.remove(j)
nam = 0
nu = 0
long = len(a)
i = 0
while long > 0:
    if abs(nam-nu) > x:
        if nam > nu and a[i]==1:
            nu+=1
            a.remove(a[i])
            long-=1
        elif nu > nam and a[i] == 0:
            nam+=1
            a.remove(a[i])
            long-=1
        else:
            print(nam+nu-1)
            exit()
    else:   
        if a[i] == 1:
            nu+=1
            a.remove(a[i])
            long-=1
        elif a[i] == 0:
            nam+=1
            a.remove(a[i])
            long-=1
print(nam+nu)
    


        





