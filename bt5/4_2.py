    a = (y-z)/(x-t)
    b = y - ((y-z)/(x-t))*x
    delta = (2*u-2*a*b+2*v*a)**2 - 4*(1+a**2)*(u**2-2*v*b+v**2-d**2)
    x1 = ((2*u-2*a*b+2*v*a) - math.sqrt(delta))/(2*(1+a**2))
    x2 = ((2*u-2*a*b+2*v*a) + math.sqrt(delta))/(2*(1+a**2))
    y1 = a*x1 + b
    y2 = a*x2 + b