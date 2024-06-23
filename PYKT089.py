n = int(input())
# de noi la cac dong tiep theo tuc la input co the co nhieu dong >.<
a = []
while len(a) < n:
    ac = list(map(int, input().split()))
    for i in range(len(ac)): a.append(ac[i])
    # print(*a)
for i in range(n):
    if a[i] % 2 == 0:
        minPos = i
        for j in range(i + 1, n):
            if a[j] % 2 == 0 and a[j] < a[minPos]: minPos = j
        x = a[i]
        a[i] = a[minPos]
        a[minPos] = x
    else:
        maxPos = i
        for j in range(i + 1, n):
            if a[j] % 2 != 0 and a[j] > a[maxPos]: maxPos = j
        x = a[i]
        a[i] = a[maxPos]
        a[maxPos] = x
print(*a)

# 10
# 1 2 3 4 5 6 7 7 9 6