from math import *
def check(s):
    if s == '0' or s == '1': return False
    for i in range(2, isqrt(int(s))):
        if int(s) % i == 0: return False
    return True

for _ in range(int(input())):
    s = input()
    s1 = s[:3]
    s2 = s[-3:]
    # print(s1, s2)
    print('YES' if (check(s1) and check(s2)) else 'NO')

# 3
# 12743
# 7337
# 12345678901234