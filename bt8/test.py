m,n = map(int,input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
print(list(zip(*ab)))