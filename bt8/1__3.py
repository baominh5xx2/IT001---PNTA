import sys
a = sys.stdin.read().strip().split('\n')
a = a[1:]
b = [list(map(int,line.strip().split())) for line in a]
print(b, sep= "\n")