s = list(input())
a = len(s) // 3
for i in range(a):
    s.insert(-(3 * (i + 1) + i), ',')
if s[0] == ',': s.pop(0)
for i in s:
    print(i, end = '')