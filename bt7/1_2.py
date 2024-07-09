n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
d = min(a)
t = max(a)
if (d >= 0 and t >= 0) or (d <=0 and t<=0):
    print((t-d)-n+1)
elif d < 0 and t >= 0:
    print((-d)+t+1 - n)
