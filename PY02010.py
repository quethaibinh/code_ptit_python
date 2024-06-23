while True:
    n = int(input())
    if n == 0: break
    maxx = 0
    minn = 10**200
    for _ in range(n):
        x = int(input())
        if x > maxx: maxx = x
        if x < minn: minn = x
    if maxx == minn: print('BANG NHAU')
    else: print(minn, maxx)


# 5
# 1
# 2
# 3
# 4
# 5
# 3
# 001
# 22
# 33333333333333333333333333333333333
# 3
# 1
# 1
# 1
# 0