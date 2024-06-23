t = int(input())
while t > 0:
    minn = 1000000000000000008
    s = input()
    s = s + 'z'
    s1 = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if i != 0 and s[i - 1].isdigit():
                minn = min(minn, s1)
                s1 = 0
        else:
            s1 = s1 * 10 + int(s[i])
    print(minn)
    t -= 1