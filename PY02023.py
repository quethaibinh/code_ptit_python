def tong(a):
    sum = 0
    while a >= 1:
        sum += a % 10
        a //= 10
    return sum

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(len(a)):
        minPos = i
        for j in range(i + 1, len(a)):
            if tong(a[minPos]) == tong(a[j]) and a[minPos] > a[j]: minPos = j
            if tong(a[minPos]) > tong(a[j]): minPos = j
        x = a[minPos]
        a[minPos] = a[i]
        a[i] = x
    print(*a)
    print()

# 1
# 8
# 143 43 22 99 7 9 1111 10000000