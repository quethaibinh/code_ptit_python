for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ac, kq = [], [1] * n
    for i in range(n):
        while len(ac) > 0 and a[ac[-1]] <= a[i]:
            ac.pop()
        kq[i] = i + 1 if len(ac) == 0 else i - ac[-1]
        ac.append(i)
    print(*kq)

# 1
# 7
# 100 80 60 70 60 75 85