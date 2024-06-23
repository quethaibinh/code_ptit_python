for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    maxx = -10000000000
    j = 0
    for i in range(n):
        if a[i] > maxx:
            maxx = a[i]
            j = i
    after = []
    a.insert(j, m)
    # print(a)
    for i in range(n + 1):
        if a[i] < 0: after.append(a[i])
    for i in range(n + 1):
        if a[i] >= 0: after.append(a[i])
    print(*after)

# 1
# 7 3
# -1 2 7 6 7 4 -1