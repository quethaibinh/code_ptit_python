from math import *
a = [1] * 1000004
def sang():
    # global a
    a[0] = 0
    a[1] = 0
    for i in range(2, 1000 + 1):
        if a[i] == 1:
            for j in range(i * i, 1000001, i):
                a[j] = 0

sang()
for _ in range(int(input())):
    res = 0
    for p in range(2, int(input()) - 5):
        if a[p] and a[p + 6] and (a[p + 4] or a[p + 2]): res += 1
    print(res)