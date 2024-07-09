n = int(input())
sum = 1
for i in range(2,int(n**0.5)+1):
    if(n%i==0):
        if i == n**0.5:
            sum+=i
        else:
            sum+=i + n/i
print(sum)
