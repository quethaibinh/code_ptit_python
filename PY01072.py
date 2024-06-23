ok = 1
b = []
a1 = []
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b.append(a[0])
cnt = 0
for i in range(1, len(a)):
    if b.count(a[i]) == 0:
        b.append(a[i])
        a1.append(cnt)
        cnt += 1
def sinh():
    global ok
    i = k - 1
    while i >= 0 and a1[i] == len(a1) - k + i + 1: i -= 1
    if i == -1: ok = 0
    else:
        a1[i] += 1
        for j in range(i + 1, k): a1[j] = a1[j - 1] + 1
while ok == 1:
    for i in range(k): print(b[a1[i]], end = ' ')
    print()
    sinh()

# 8 3
# 2 4 4 3 5 1 3 4