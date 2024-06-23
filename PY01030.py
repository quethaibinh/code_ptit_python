def uoc(a, b):
    if b == 0: return a
    return uoc(b, a % b)

n, k = map(int, input().split())
cnt = 0
for i in range(10 ** (k - 1), 10 ** k):
    if uoc(i, n) == 1:
        print(i, end = ' ')
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0
