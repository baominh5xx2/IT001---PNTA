h = []
while True:
    try:
        l=input()
    except EOFError:
        break
    for i in l.split():
        if i!='':
            h.append(int(i))
n = h[0]
for i in range(1,n+1):
    k = str(h[i])
    if len(k) % 2 == 0:
        newstr = int(k[(len(k)//2)-1:(len(k)//2)+1])
        a.append(newstr)
    else:
        newstr = int((k[len(k)//2]))
        a.append(newstr)
maxw = max(a)
for j in range(len(a)-1,-1,-1):
    if(a[j] ==  maxw):
        index = j
        break
print(h[index+1])
