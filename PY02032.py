s = input()
dic = {}
a = []
for i in range(0, len(s), 2):
    x = int(s[i:i + 2])
    if x in dic: dic[x] += 1
    else: dic[x] = 1
for i in dic:
    a.append(i)
a.sort()
if len(s) % 2 != 0: a.pop(0)
print(*a)