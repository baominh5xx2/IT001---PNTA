import math
x,y,n,m = map(int,input().split())
def s(x,y,n,m):
    if n == 0: return 0
    if m <= x: return n
    return s(x+y,y,n-1,m) + math.cell(m/x)
print(s(x,y,n,m))