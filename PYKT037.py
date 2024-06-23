p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def check(n, b):
    a = []
    if b <= 10:
        while n > 0:
            a.append(n % b)
            n //= b
    else:
        while n > 0:
            if n % b < 10: a.append(n % b)
            else: a.append(p[n % b - 10])
            n //= b
    return a


for _ in range(int(input())):
    n, b = map(int, input().split())
    a = check(n, b)
    for i in range(-1, -len(a) - 1, -1): print(a[i], end = '')
    print()

# 3
# 10 2
# 2021 2
# 31 16