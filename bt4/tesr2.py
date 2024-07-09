h = []
while True:
    try:
        l=input()
    except EOFError:
        break
    for i in l.split():
        if i!='':
            h.append(int(i))
c=[]
n = h[0]
for i in range (n):
    b=[]
    a=str(input())
    b+=list(map(int,a))
    if len(b)%2==0:
        c+=[int(''.join(str(i) for i in b[len(b)//2-1:len(b)//2+1]))]
    else:
        c+=[b[(len(b)-1)//2]]
    if max(c)==int(''.join(str(i) for i in b[len(b)//2-1:len(b)//2+1])) \
       or max(c)==b[(len(b)-1)//2]:
        z=a
print(z)

