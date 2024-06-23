for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    cnt = 0
    if len(a) != 1:
        for j in range(1, len(a)):
            if a[j] != a[j - 1]: cnt += (a[j] - a[j - 1] - 1)
    print(cnt)
    # print(*a)

# 2
# 5
# 4 5 3 8 6
# 3
# 2 1 3