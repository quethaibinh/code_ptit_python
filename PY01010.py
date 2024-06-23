for t in range(int(input())):
    s = input()
    x = int(s[0]) * 10 + int(s[1])
    y = int(s[-2]) * 10 + int(s[-1])
    if x == y: print('YES')
    else: print('NO')