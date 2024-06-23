def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]: return False
    return True

for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    print('YES' if check(a, b) else 'NO')

# 2
# 4
# 7 5 3 2
# 5 4 8 7
# 8
# 7 5 3 2 5 105 45 10
# 2 4 0 5 6 9 75 84