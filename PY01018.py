p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    s = input()
    if s == '0': break
    k, s1 = s.split()
    s2 = []
    for i in s1:
        s2.append(p[(p.index(i) + int(k)) % 28])
    s2 = s2[::-1]
    for i in s2: print(i, end = '')
    print()

# 1 ABCD
# 14 ROAD
# 0