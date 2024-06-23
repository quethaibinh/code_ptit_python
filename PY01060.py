def tinh(s):
    tong = 0
    tich = 1
    check = False
    for i in range(len(s)):
        if i % 2 != 0: tong += int(s[i])
        else:
            if s[i] != '0':
                check = True
                tich *= int(s[i])
    print(f'{tich} {tong}' if check else f'0 {tong}')

for _ in range(int(input())):
    tinh(input())

# 3
# 12345678
# 20000
# 22334455667788