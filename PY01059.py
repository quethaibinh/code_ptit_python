def bt(s):
    tong = 0
    tich = 1
    check = False
    for i in range(len(s)):
        if i % 2 == 0: tong += int(s[i])
        else:
            if s[i] == '0': continue
            check = True
            tich *= int(s[i])
    return (tong, tich) if check else (tong, 0)

for _ in range(int(input())):
    for i in bt(input()):
        print(i, end = ' ')
    print()

# 3
# 12345678
# 20000
# 22334455667788