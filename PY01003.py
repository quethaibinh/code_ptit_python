for t in range(int(input())):
    s = list(int(i) for i in input())
    if len(s) <= 1: print(s[0])
    else:
        for i in range(-1, -len(s), -1):
            if s[i] >= 5:
                s[i] = 0
                s[i - 1] += 1
            else:
                s[i] = 0
        if s[-len(s)] == 10:
            s[-len(s)] = 10
        for i in s:
            print(i, end = '')
        print()