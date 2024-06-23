def tich(s):
    t = 1
    for i in s:
        if i == '0': continue
        t *= int(i)
    return t

for _ in range(int(input())):
    print(tich(input()))

# 2
# 123410
# 123456789123456789