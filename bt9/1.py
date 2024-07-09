def main():
    #n,k = map(int,input().split())
    a = [0]
    j = 0
    dem = 0
    while j < 9:
            if j % 2 == 0:
                for i in range(0,len(a)):
                    if a[i] == 0:
                            a += [1]
                            dem += 1
                    elif a[i] == 1:
                            a += [0]
                            dem += 1
            else:
                a = a + a[len(a)-1::-1]
            j += 1
    #print(a)
    print(a)
main()  

