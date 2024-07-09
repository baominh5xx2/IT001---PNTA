n = int(input())\

import math
def checkcp(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return True
    else:
        return False
dem = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if checkcp(i*j) == True:
            dem += 1
            print(i,j)
print(dem)