for _ in range(int(input())):
    n, p = map(int, input().split())
    cnt, k = 0, 1
    x = p ** k
    while(x < n):
        cnt += (n // x)
        k += 1
        x = p ** k
    print(cnt)

# 3
# 62  7
# 76  2
# 3  5