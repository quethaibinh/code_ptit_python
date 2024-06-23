s = input()
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
for i in range(len(a)):
    print(a[i], dic[a[i]])
