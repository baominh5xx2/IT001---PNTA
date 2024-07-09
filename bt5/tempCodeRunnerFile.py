import math
x,y,z,t,u,v,d = map(int,input().split())
ux = x - z
uy = y - t
nx = -uy
ny = ux
dis = abs((u*nx+v*ny-x*nx-y*ny)/math.sqrt((z-x)**2+(y-t)**2))
if dis - int(dis)==0:
    dis = int(dis)
if dis > d:
    print(0)
elif dis  == d :
    print(1)
else:
    if ux == 0 or uy == 0:
        dem = 0
        if ux == 0:
            if y < t:
                for i in range(y,t+1):
                    if  (i-v)**2 + (x-u)**2<= d**2:
                        dem+=1
            if y > t:
                for i in range(t,y+1):
                    if  (i-v)**2 + (x-u)**2<= d**2:
                        dem+=1
        else:
            if x < z:
                for i in range(x,z+1):
                    if (i-u)**2 + (y-v)**2<= d**2:
                        dem+=1
            else:
                   for i in range(z,x+1):
                    if (i-u)**2 + (y-v)**2<= d**2:
                        dem+=1
        print(dem)
        exit()
    else:
            dem = 0
            a = (y-t)/(x-z)
            b = y - a*x
            delta = (2*u-2*a*b+2*v*a)**2 - 4*(1+a**2)*(u**2-2*v*b+v**2-d**2+b**2)
            x1 = ((2*u-2*a*b+2*v*a) - math.sqrt(delta))/(2*(1+a**2))
            x2 = ((2*u-2*a*b+2*v*a) + math.sqrt(delta))/(2*(1+a**2))
            y1 = a*x1 + b
            y2 = a*x2 + b
            if x < z:
                for i in range(x,z+1):
                    if (i-u)**2 + ((a*i+b)-v)**2 <= d**2 and ((a*i+b)-int(a*i+b))==0:
                        dem+=1
            elif x > z:
                for i in range(x,z-1,-1):
                    if (i-u)**2 + ((a*i+b)-v)**2 <= d**2 and ((a*i+b)-int(a*i+b))==0:
                        dem+=1
            print(dem)



