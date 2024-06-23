for _ in range(int(input())):
    n = int(input())
    dic = {}
    maxx = 0
    for _ in range(n):
        x = int(input())
        if x in dic : dic[x] += 1
        else: dic[x] = 1
        maxx = max(maxx, dic[x])
    ans = 10000
    for i in dic:
        if dic[i] == maxx:
            ans = min(ans, i)
    print(ans)

# 3
# 3
# 999
# 999
# 19
# 4
# 13
# 333
# 333
# 13
# 3
# 11
# 12
# 13
