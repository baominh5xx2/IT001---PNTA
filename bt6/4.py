n = list(map(int,list(input())))
for i in range(int(n[0]),9):
    if(i+int(''.join(map(str,n[2:len(n)-1]))))%3==0:
        print(i)=   