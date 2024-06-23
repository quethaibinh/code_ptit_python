def tich(a):
    t = 1
    while a >= 1:
        t *= (a % 10)
        a //= 10
        if t == 0: return 0
    return t

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(len(a)):
        minPos = i
        for j in range(i + 1, len(a)):
            if tich(a[minPos]) == tich(a[j]) and a[minPos] > a[j]: minPos = j
            if tich(a[minPos]) > tich(a[j]): minPos = j
        x = a[minPos]
        a[minPos] = a[i]
        a[i] = x
    print(*a)

# 1
# 8
# 143 43 22 99 7 9 1111 10000000