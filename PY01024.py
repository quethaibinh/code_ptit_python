def check(s):
    tong = int(s[0])
    for i in range(1, len(s)):
        tong += int(s[i])
        if abs(int(s[i]) - int(s[i - 1])) != 2:
            print('NO')
            return
    if tong % 10 != 0:
        print('NO')
        return
    print('YES')

for _ in range(int(input())):
    check(input())

# 3
# 1353
# 246864
# 123435