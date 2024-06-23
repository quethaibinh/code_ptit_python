from math import *
for _ in range(int(input())):
    a = int(input())
    print('1', end = '')
    for i in range(2, int(sqrt(a))):
        if a % i == 0:
            cnt = 0
            while a % i == 0:
                cnt += 1
                a //= i
            print(f' * {i}^{cnt}', end = '')
    if a != 1: print(f' * {a}^1')
    print()

# 3
# 28
# 100
# 1234