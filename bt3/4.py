
def ktra(n):
    return len([i for i in range(1,n+1) if n%i==0]) == 2
for  i in range(2000):
    print(f'i = {i}, ktra(i) = {ktra(i)} ')
    