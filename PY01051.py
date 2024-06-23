def check(s):
    if s / 10 < 1: return False
    s1 = s;
    s2 = 0;
    while s >= 1:
        s2 = s2 * 10 + s % 10;
        s //= 10;
    if s2 == s1: return True
    return False

for _ in range(int(input())):
    s = input()
    tong = 0;
    for i in range(len(s)):
        tong += int(s[i])
    print('YES' if check(tong) else 'NO')


# 2
# 12341
# 22222222222222222222