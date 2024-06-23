def dao(a):
    b = 0
    while a >= 1:
        b = b * 10 + a % 10
        a //= 10
    return b
# s = int(input())
# print(dao(s))

for _ in range(int(input())):
    tong = int(input())
    cnt = 0
    while cnt <= 1000 and tong % 7 != 0:
        tong = tong + dao(tong)
        cnt += 1
    if tong % 7 == 0: print(tong)
    else: print('-1')

# 5
# 1
# 2
# 3
# 4
# 999999