def sum(a, b, i1, j1):
    sum1 = 0
    for i in range(3):
        for j in range(3):
            sum1 += (a[i1 + i][j1 + j] * b[i][j])
    return sum1

for _ in range(int(input())):
    n, m = map(int, input().split())
    a, ke, kq = [], [], 0
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(3):
        ke.append(list(map(int, input().split())))
    # for i in range(3):
    #     print(ke[i])
    for i in range(n - 2):
        for j in range(m - 2):
            kq += sum(a, ke, i, j)
            # print(kq)
    print(kq)

# 2
# 4 4
# 2 1 0 0
# 3 2 1 1
# 4 3 2 1
# 2 2 1 0
# -1 -1 -1
# -1 8 -1
# -1 -1 -1
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 1 1 1
# 1 1 1
# 1 1 1