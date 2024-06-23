for _ in range(int(input())):
    s = input()
    sc = input()
    a = [0] * len(s)
    cnt = 0
    i = 0
    while i < len(s):
        if a[i] == 0:
            s1 = s[i: (i + len(sc))]
            if sc == s1:
                cnt += 1
                for j in range(i, i + len(sc)): a[j] = 1
                i += (len(sc) - 1)
        i += 1
    print(cnt)

# 2
# 1212121112211221121
# 121
# 2222222222322292
# 2222