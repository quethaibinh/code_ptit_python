for _ in range(int(input())):
    s = input()
    check = True
    if len(s) < 3: check = False
    else:
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                check = False
                break
            if s[i] < s[i - 1]:
                for j in range(i + 1, len(s)):
                    if s[j] >= s[j - 1]:
                        check = False
                        break
                break
    if check: print('YES')
    else: print('NO')

# 3
# 12342
# 23342
# 5678961