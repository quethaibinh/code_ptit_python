def thap(s):
    sc = 0
    while len(s) < 3: s = '0' + s
    for i in range(-1, -len(s) - 1, -1):
        sc += int(s[i]) * (2 ** (-i - 1))
    return sc

def chuyen(s):
    cs = ''
    for i in range(-1, -len(s) - 1, -3):
        s1 = s[i: i - 3: -1]
        s1 = s1[::-1]
        # print(s1)
        cs = str(thap(s1)) + cs
    return cs
# chuyen(input())
print(chuyen(input()))