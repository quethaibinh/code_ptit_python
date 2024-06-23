for _ in range(int(input())):
    s = input()
    se = set(s)
    if len(se) == 2:
        check = True
        for i in range(2, int(len(s)), 2):
            if s[i] != s[0]: check = False
        for i in range(3, int(len(s)), 2):
            if s[i] != s[1]: check = False
        if check: print('YES')
        else: print('NO')
    else: print('NO')