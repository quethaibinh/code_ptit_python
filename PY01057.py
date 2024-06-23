from math import *
def nt(s):
    if s == 0 or s == 1: return False
    for i in range(2, int(sqrt(s)) + 1):
        if s % i == 0: return False
    return True

def check(s):
    for i in range(len(s)):
        if s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i] == '7':
            if not nt(i): return False
        else:
            if nt(i): return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')

# 2
# 14239567
# 2314514535353