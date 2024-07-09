a = int(input())
b = int(input())
socay = a
def luoi(a,b,socay):
    if a < b:
        return socay
    elif a == 1:
        return a+1
    else:
        if a >= b:
            socay += a//b
    print(a+(int(a/b) - int(a/b)*b),socay)
    return luoi(a+(int(a/b) - int(a/b)*b),b,socay)
print(luoi(a,b,socay))