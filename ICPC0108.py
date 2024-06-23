for _ in range(int(input())):
    n = int(input())
    li = sorted(list(map(int, input().split())))
    res = 0
    # print(li)
    for l in range(len(li) - 2):
        m= l + 1
        r = len(li) - 1
        while m < r:
            sum = li[l] + li[m] + li[r]
            if sum > 0: r -= 1
            elif sum < 0: m += 1
            else:
                res += 1
                m += 1
    print(res)

# 2
# 5
# 0 -1 2 -3 1
# 5
# 1 -2  1  0  5