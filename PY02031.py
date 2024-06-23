nt = [1] * 1000004
def sang():
    nt[0] = nt[1] = 0
    for i in range(1001):
        if nt[i]:
            for j in range(i * i, 1000001, i):
                nt[j] = 0
sang()
n, m = map(int, input().split())
a = []
for  i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if nt[a[i][j]]: a[i][j] = 1
        else: a[i][j] = 0
for i in range(n):
    print(*a[i])

# 3 3
# 1 2 3
# 4 5 6
# 7 8 9