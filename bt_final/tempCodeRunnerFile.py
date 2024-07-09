n = input()
def verso(n):
    n = list(n)
    k = []
    for i in range(0,len(n)):
        if n[i] != '0':
            k = n[i::]
            return k
k = verso(n)
print(len(set(''.join(map(str,k)))))