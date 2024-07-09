s1 = list(input())
s2 = list(input())
if (s1[0] == '#' and s2[1] == '#' and s1[1] == '.' and s2[0] =='.') or s1[1] == '#' and s2[0] == '#' and s1[0] == '.' and s2[1] =='.':
    print("No")
else:
    print("Yes")