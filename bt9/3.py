import sys
import re
a = re.split('\n+', sys.stdin.read().strip())[:-1]
b = [re.split('(\d+)',i) for i in a]    
def convert(x):
    try:
        return int(x)
    except:
        return x
b = [list(map(convert,i)) for i in b]
b.sort()
print(''.join(map(str,min(b))))
print(''.join(map(str,max(b))))

 