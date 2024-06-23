n = int(input())
a, x, kq = [], [], []
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(n):
        x.append([0] * n)
        kq.append([0] * n)
for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1: x[i][j] = 1
for i in range(n):
    for j in range(n):
        for k in range(n):
            kq[i][j] += (a[i][k] *x[k][j])

for i in range(n): print(*kq[i])