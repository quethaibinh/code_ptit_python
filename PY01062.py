from math import *
def check(s):
    cnt1 = 0
    if len(s) == 0 or len(s) == 1: return False
    for i in range(2, isqrt(len(s))):
        if len(s) % i == 0: return False
    for i in s:
        if i == '2' or i == '3' or i == '5' or i == '7': cnt1 += 1
    if cnt1 < len(s) - cnt1: return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')

# 3
# 1234567
# 22334455667
# 23400300489898989