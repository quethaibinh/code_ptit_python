n, m = map(int, input().split())
a = list(map(int, input().split()))
dic = {}
maxx, max2 = 0, 0
gtri = 100005
for i in range(n):
    if a[i] in dic: dic[a[i]] += 1
    else: dic[a[i]] = 1
    maxx = max(maxx, dic[a[i]])
for i in dic:
    if dic[i] != maxx: max2 = max(max2, dic[i])
for i in dic:
    if dic[i] == max2: gtri = min(gtri, i)
if max2 == 0: print('NONE')
else: print(gtri)

# 10 4
# 2 3 1 2 3 1 1 2 3 2

# 8 4
# 1 2 3 4 4 3 2 1

