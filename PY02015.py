from math import *
while True:
    check, check1 = True, False
    cnt = 0
    a = list(map(int, input().split()))
    for i in range(4):
        if a[i] != 0:
            check = False
            break
    if check: break
    for i in range(1, 4):
        if a[i] != a[i - 1]:
            check1 = True
            break
    while check1:
        check2 = False
        x = a[0]
        for i in range(3): a[i] = abs(a[i] - a[i + 1])
        a[3] = abs(a[3] - x)
        for i in range(1, 4):
            if a[i] != a[i - 1]:
                check2 = True
                break
        if not check2: check1 = False
        cnt += 1
        # for i in range(4): print(a[i], end = ' ')
        # print()
    print(cnt)


# 1 3 5 9
# 4 3 2 1
# 0 0 0 0