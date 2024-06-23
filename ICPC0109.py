
for _ in range(int(input())):
    n = input()
    a = list(int(i) for i in input().split())
    print(a)
    sum = 0
    minSum = 100000000000000000000
    tryy(0, sum, minSum)
    print(minSum)


# 2
# 7
# 1 2 3 0 -1 8 10
# 7
# 9 8 20 3 4 -1 0