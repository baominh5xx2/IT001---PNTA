n = int(input())
ab = [[0 for j in range(n)] for i in range(n)]
h =[]
dem = 0
while True:
    try:
        l=input()
    except EOFError:
        break
    for i in l.split():
        if i!='':
            h.append(int(i))
            dem += 1
        if int(i) != 0 and int(i) != 1:
            print("false")
            exit()
if dem != n*n:
    print("false")
    exit()
else:
    m = 0
    for i in range(0,n):
        for j in range(0,n):
            ab[i][j] = h[m]
            m += 1
def ktra(ab):
    col = len(ab[0])
    row = len(ab)
    if col != row:
        return False
    if row == 0:
        return False
    for i in range(0,n):
        for j in range(0,n):
            if i == j and ab[i][j] != 1:
                return False
            elif i != j and ab[i][j] != 0:
                return False
    return True
if ktra(ab):
    print("true")
else:
    print("false")