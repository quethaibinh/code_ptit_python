for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    a1 = a[-len(a) + d:]
    a2 = a[:d]
    for i in a1: print(i, end = ' ')
    for i in a2: print(i, end = ' ')
    print()

# 2
# 5 2
# 1 2 3 4 5
# 10 3
# 2 4 6 8 10 12 14 16 18 20