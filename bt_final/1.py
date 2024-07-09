m = int(input())
h = ['was','swa']
'''while True:
    try:
        l=input()
    except EOFError:
        break
    for i in l.split():
        if i!='':
            h.append(i)'''
k = []
g = []
k1 = []
g1 = []
for i in range(0,m*2,2):
    s = list(h[i])
    s1 = list(h[i+1])
    if len(s) != len(s1):
        print("NO")
        exit()
    for i in range(0,min(len(s),len(s1))):
        k.append(s[i])
        g.append(s1[i])
    for j in range(0,min(len(k),len(g))-1):
        if k.index(k[j]) == g.index(k[j+1]):
            print("NO") 
    else:
         print("YES")
    k.clear()
    g.clear()
    k1.clear()
    g1.clear()
