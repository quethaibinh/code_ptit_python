def check(s):
    tong = 0
    for i in s: tong += int(i)
    print('YES' if tong % 3 == 0 else 'NO')

for _ in range(int(input())):
    check(input())

# 2
# 12341
# 123456789123456789