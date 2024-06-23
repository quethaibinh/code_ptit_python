for t in range(int(input())):
    s = input()
    check = True
    for i in s:
        if int(i) != 4 and int(i) != 7:
            check = False
            break
    if check: print('YES')
    else: print('NO')