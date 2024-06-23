a = [1] * 1000001
def sng():
    a[0] = a[1] = 0
    for i in range(2, 1001):
        if a[i]:
            for j in range(i * i, 1000001, i):
                a[j] = 0

sng()
a1 = []
cnt = 0
for i in range(2, 1000001):
    if a[i]: a1.append(i)
n, x = map(int, input().split())
print(x, end = ' ')
for i in range(n):
    x += a1[i]
    print(x, end = ' ')