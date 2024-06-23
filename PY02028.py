nt = [1] * 1000005
def sng():
    nt[0] = nt[1] = 0
    for i in range(2, 1001):
        if nt[i]:
            for j in range(i * i, 1000001, i):
                nt[j] = 0
sng()

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if nt[a[i]]:
        minPos = i
        for j in range(i + 1, n):
            if nt[a[j]] and a[j] < a[minPos]: minPos = j
        tmp = a[minPos]
        a[minPos] = a[i]
        a[i] = tmp
for i in a:
    print(i, end = ' ')

# 8
# 4 6 3 8 7 2 5 9