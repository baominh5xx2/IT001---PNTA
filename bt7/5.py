'''p = []
while True:
    try:
        line = input()
    except EOFError:
        break
    for i in line.split():
        if i != '':
            p.append(int(i))
s= p[0]
d = p[1]
c = p[2]'''
s = 15
d = 2
c = 9
giua = (c+d)/2
target = (giua+c)/2
sum = d
def cut(n):
    if n - int(n) == 0:
        n = int(n)
    return n
if s % 2 != 0:
    target1 = (abs(giua - target))/(((s+1)//2 -3))
    if d > c:
        while sum >= c:
            print(cut(sum))
            sum-=target1
    else:
        while sum <= c:
            print(cut(sum))
            sum+=target1
else:
    target1 = (abs(giua - target))/((s+1)//2 -3)
    if d > c:
        while sum >= c:
            if sum != giua:
                print(cut(sum))
                sum-=target1
            elif sum == giua:
                print(cut(sum))
                print(cut(sum))
                sum -=target1
    else:
        while sum <= c:
            if sum != giua:
                print(cut(sum))
                sum+=target1
            elif sum == giua:
                print(cut(sum))
                print(cut(sum))
                sum +=target1