def uoc(a, b):
    if b == 0: return a
    return uoc(b, a % b)

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    min_len = 10000001
    i = 0
    ac = []
    while i < n:
        j = i + 1
        check = True
        if a[i] % k == 0:
            ac.append(a[i])
            while j < n and check:
                for k1 in range(len(ac)):
                    if uoc(ac[k1], a[j]) != k:
                        check = False
                        break
                if check:
                    ac.append(a[j])
                    j += 1
            if len(ac) != 1: min_len = min(min_len, len(ac))
            if a[i] == k and len(ac) == 1: min_len = 1
            ac.clear()
        i = j
    if min_len != 10000001: print(min_len)
    else: print(-1)



# 3
# 8 3
# 6 9 7 10 12 24 36 27
# 4 3
# 2 4 6 8
# 4 6
# 1 2 3 6
