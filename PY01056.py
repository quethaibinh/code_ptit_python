from math import *

def check(s):
    tong = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if int(s[i]) % 2 != 0: return False
        else:
            if int(s[i]) % 2 == 0: return False
        tong += int(s[i])
    if tong == 0 or tong == 1: return False
    for i in range(2, int(sqrt(tong))):
        if tong % i == 0: return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')

# 2
# 2345678521
# 1212121212121212121212121