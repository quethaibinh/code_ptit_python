for _ in range(int(input())):
    s = input()
    print('YES' if all((s[i] == '0' or s[i] == '1' or s[i] == '2') for i in range(len(s))) else 'NO')

# 3
# 1214AB
# 10210221
# 22222222