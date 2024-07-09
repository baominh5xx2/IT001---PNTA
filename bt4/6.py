n = int(input())
a = n - 1
dem = 0
import math
if n > 200:
    while n > 0:
        b = math.sqrt(n*n - a*a)
        if b == int(b) and a >= int(b):
            dem+=1
            a-=1
        elif a < int(b):
            print(dem)
            exit()
        if a % 2 == 0:
            a-=2
        else:
            a-=1
else:
    while n > 0:
        b = math.sqrt(n*n - a*a)
        if b == int(b) and a >= int(b):
            dem+=1
        elif a < int(b):
                print(dem)
                exit()
        a-=1