for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    cnt = 0
    for i in range(n):
        if abs(a[i]) in dic: dic[abs(a[i])] += 1
        else: dic[abs(a[i])] = 1
    for i in dic:
        if dic[i] == 1 or i == 0: cnt += 1
        else: cnt += 2
    print(cnt)

# 2
# 4
# 1 -1 2 2
# 3
# 1 2 3