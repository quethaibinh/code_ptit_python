s = input()
k = int(input())
n = len(s)
if len(s) % 2 != 0: n = len(s) - 1
dic = {}
a = []
for i in range(0, n, 2):
    x = int(s[i:i + 2])
    if x in dic: dic[x] += 1
    else:
        dic[x] = 1
        a.append(x)
check = False
a.sort()
for i in range(len(a)):
   if dic[a[i]] >= k:
       print(a[i], dic[a[i]])
       check = True
if not check: print('NOT FOUND')

# 124356141111434356149
# 2

# 124356141111434356149
# 10