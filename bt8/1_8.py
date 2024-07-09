a1 = []
while True:
    b = input()
    if b == '.':
        break
    a1.append(b)
key = input()
thuongkey = key.lower()
kq = []
for a2 in a1:
    thuongb = a2.lower()
    index = thuongb.find(thuongkey)
    if index != -1:
        kq1 = a2[:index] + '[' + a2[index:index+len(key)] + ']' + a2[index+len(key):]
        print(kq1)