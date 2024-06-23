def kt(s):
    for i in range(1, int(len(s)), 1):
        if int(s[i]) < int(s[i - 1]):
            return False
    return True

for t in range(int(input())):
    s = input()
    if kt(s): print('YES')
    else: print('NO')