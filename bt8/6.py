import sys
a = [l for l in sys.stdin.read().strip().split('\n')]
d = 0
case_line = 0
while True:
    m, n = map(int, a[case_line].split())
    temp = a[case_line + 1:case_line + m + 1]
    temp = [[i for i in line] for line in temp]
    def bucket_fill(a,i,j):
        if i < 0 or j < 0 or i >= len(a) or j >= len(a[0]):
            return
        if a[i][j] != '-':
            return
        a[i][j] = '!'
        bucket_fill(a,i - 1,j)
        bucket_fill(a,i + 1,j)
        bucket_fill(a,i,j - 1)
        bucket_fill(a,i,j + 1)
    count = 0
    for so_hang, hang in enumerate(temp):
        for so_cot, cot in enumerate(hang):
            if cot == '-':
                count += 1
                bucket_fill(temp,so_hang,so_cot)
    d += 1
    print(f"Case {d}: {count}")
    case_line += m + 1
    if case_line >= len(a):
        break