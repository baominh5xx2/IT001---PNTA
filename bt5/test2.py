import math
x,y = map(int,input().split())
z,t = map(int,input().split())
u,v = map(int,input().split())
d = int(input())
dis = abs((u*(z-x)+v*(y-t)-x*(z-x)-y*(y-t))/math.sqrt((z-x)**2+(y-t)**2))
print(dis)