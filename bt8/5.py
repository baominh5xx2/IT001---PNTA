n = 3
x = []
y = []
for i in range(0, n):
    k = list(map(int, input().split()))
    x.append(k[0])
    y.append(k[1])
dem = 0 
for i in range(2, n):
    x1 = x[i-1] - x[i-2]
    y1 = y[i-1] - y[i-2]
    x2 = x[i] - x[i-1]
    y2 = y[i] - y[i-1]
    if y1 == 0:
        if x1 > 0:
            if x2 == 0 and y2 < 0:
                dem += 1
        elif x1 < 0:
            if x2 == 0 and y2 > 0:
                dem += 1
    elif x1 == 0:
        if y1 > 0:
            if y2 == 0 and x2 > 0:
                dem += 1
        elif y1 < 0:
            if y2 == 0 and x2 < 0:
                dem += 1
print(dem)



