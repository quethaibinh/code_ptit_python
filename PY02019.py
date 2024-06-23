def uoc(a, b):
    if b == 0: return a
    return uoc(b, a % b)
n = int(input())
a = sorted(list(map(int, input().split())))
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if uoc(a[i], a[j]) == 1: print(a[i], a[j])

# 5
# 3 7 9 6 13