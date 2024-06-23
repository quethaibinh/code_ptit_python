nt = [1] * 1000006
def sng():
    nt[0] = nt[1] = 0
    for i in range(2, 1001):
        if nt[i]:
            for j in range(i * i, 1000001, i):
                nt[j] = 0
sng()
def check(x):
    i1, i2 = x, x
    while not nt[i1]: i1 += 1
    while not nt[i2]: i2 -= 1
    return min(i1 - x, x - i2)

n = int(input())
a = list(map(int, input().split()))
minCnt = 0
for i in range(n):
    if not nt[a[i]]: minCnt = max(minCnt, check(a[i]))
print(minCnt)

# 8
# 13 5 8 7 9 15 26 34