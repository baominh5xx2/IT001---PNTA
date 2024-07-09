a = int(input())
b = int(input())
du = a
cay = a
while du > 0:
    if du >= b:
        cay+= int(du/b)
    else:
        break
    du += int(du/b) - int(du/b)*b 
print(cay)