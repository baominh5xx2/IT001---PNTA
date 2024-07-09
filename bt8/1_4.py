ab = []
for i in range(4):
    row = list(map(int, input().split()))
    ab.append(row)

while True:
    try:
        move = input()
        if move:
            break
    except:
        pass
def dichuyen(l):
    k = [0]*4
    index = 0
    for i in range(0,4):
        if l[i] != 0:
            if k[index] == 0:
                k[index] = l[i]
            elif k[index] == l[i] and l[i] != 2048:
                k[index] *= 2
                index += 1
            else:
                index += 1
                k[index] = l[i] 
    return k
r = [[0]*4 for _ in range(4)]
if move == 'L':
    r = [dichuyen(m) for m in ab]
elif move == 'R':
    r = [dichuyen(ab[i][::-1])[::-1] for i in range(4)]
elif move == 'U':
    r = [dichuyen(col) for col in list(zip(*ab))]
    r = list(map(list, zip(*r)))
elif move == 'D':
    col = list(zip(*ab[::-1]))
    r = [dichuyen(col1)[::-1] for col1 in col]
    r = list(map(list, zip(*r)))
for i in range(0,4):
    for j in range(0,4):
        print(r[i][j], end= ' ')
    print()