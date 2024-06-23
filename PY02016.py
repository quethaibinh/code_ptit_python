def check(a):
    dic = {}
    cnt, ans = 0, 10000000
    for i in range(len(a)):
        if a[i] in dic: dic[a[i]] += 1
        else: dic[a[i]] = 1
        cnt = max(cnt, dic[a[i]])
    if cnt > len(a) // 2:
        # return cnt
        for i in dic:
            if dic[i] == cnt: ans = min(i, ans)
        return ans
    return 'NO'

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(check(a))

# 2
# 9
# 3 3 4 2 4 4 2 4 4
# 8
# 3 3 4 2 4 4 2 4