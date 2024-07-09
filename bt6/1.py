x,y,n,m = map(int,input().split())
import sys
sys.setrecursionlimit(15000)
count = 0
def damage(x,n,count):
    if n == 0:
        return count
    else:
        if(m%x != 0):
          count +=int(m/x)
          count +=1 
        else:
          count +=int(m/x)
        return damage(x+y,n-1,count)
print(damage(x,n,count))
