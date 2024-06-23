s = input()
n = len(s)
if len(s) % 2 != 0: n = len(s) - 1
dic = {}
a = []
for i in range(0, n, 2):
    x = int(s[i:i + 2])
    if x in dic: continue
    else:
        dic[x] = 1
        a.append(x)
print(*a)