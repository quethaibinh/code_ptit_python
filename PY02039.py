from math import *
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
u, d = 0, 0
for i in range(n):
    for j in range(i):
        u += a[i][j]
    for j in range(i + 1, n):
        d += a[i][j]
print('YES' if abs(u - d) < k else 'NO')
print(abs(u - d))
# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5