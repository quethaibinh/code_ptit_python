from math import *
for _ in range(int(input())):
    s = input()
    s2 = s[::-1]
    check = True
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            check = False
    if check: print('YES')
    else: print('NO')

# 2
# acxz
# bcxz