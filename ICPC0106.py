import math
for i in range(int(input())):
    n = int(input())
    s = input()
    s = s[::-1]
    thap = 0
    # print(s)
    for j in range(len(s)):
        thap += (int(s[j]) * (2 ** int(j)))
    s1 = ''
    while thap > 0:
        ans = int(thap % n)
        if ans == 10:
            ans = 'A'
        if ans == 11:
            ans = 'B'
        if ans == 12:
            ans = 'C'
        if ans == 13:
            ans = 'D'
        if ans == 14:
            ans = 'E'
        if ans == 15:
            ans = 'F'
        s1 += str(ans)
        thap //= n
    s1 = s1[::-1]
    print(str(s1))
