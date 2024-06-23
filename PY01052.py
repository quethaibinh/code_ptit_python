from math import *

def check(s):
    tong = 0
    for i in s: tong += int(i)
    if tong == 0 or tong == 1: return False
    for i in range(2, int(sqrt(tong)) + 1):
        if tong % i == 0: return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')

# 2
# 12341
# 22222222222222222222