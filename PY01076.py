def uoc(a, b):
    if b == 0: return a
    return uoc(b, a % b)
for _ in range(int(input())):
    s1 = int(input())
    s2 = int(input())
    print(uoc(s1, s2))


# 1
# 1221
# 1234567891011121314151617181920212223242526272829