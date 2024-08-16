s = input()
s1 = ''
for i in s:
    if not (i >= '0' and i <= '9'): s1 += ' '
    else: s1 += i
a = list(map(int, s1.split()))
print("YES" if a[0] + a[1] == a[2] else "NO")