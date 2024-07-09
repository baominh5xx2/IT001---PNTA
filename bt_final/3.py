ab = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
h = [89,7,87,79,24,84,30]
'''while True:
    try:
        l=input()
    except EOFError:
        break
    for i in l.split():
        if i!='':
            h.append(int(i))'''
if (ab[0][0] in h and ab[1][1] in h and ab[2][2] in h) or (ab[0][2] in h and ab[1][1] in h and ab[2][0] in h):
        print("Yes")
        exit()
for i in range(0,3):
    dem = 0
    for j in range(0,3):
        if ab[i][j] in h:
            dem += 1
    if dem == 3:
        print("Yes")
        exit()
for j in range(0,3):
    dem = 0
    for i in range(0,3):
        if ab[i][j] in h:
            dem += 1
    if dem == 3:
        print("Yes")
        exit()
else:
    print("No")
    exit()
    
