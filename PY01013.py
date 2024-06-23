from math import*

def uoc(a, b):
    if b == 0: return a
    return uoc(b, a % b)

def check(a):
    cnt = 0
    for i in a:
        cnt += int(i)
    if cnt == 0 or cnt == 1: return False
    for i in range(2, int(sqrt(cnt)) + 1, 1):
        if cnt % i == 0:
            return False
    return True

for t in range(int(input())):
    a, b = map(int, input().split())
    if check(str(uoc(a, b))): print('YES')
    else: print('NO')
