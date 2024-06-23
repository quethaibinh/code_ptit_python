def check(a, b):
    if b == 0: return a
    return check(b, a % b)

for _ in range(int(input())):
    s = input()
    s2 = s[::-1]
    if check(int(s), int(s2)) == 1: print('YES')
    else: print('NO')

# 2
# 123
# 997