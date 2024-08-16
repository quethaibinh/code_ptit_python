for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for _ in range(3):
        min = 100000000000
        index = 0
        for i in range(len(a)):
            if min >= a[i]: 
                min = a[i]
                index = i
        sum += min
        a.pop(index)
        # print(*a)
    print(sum)



# 2
# 7
# 1 2 3 0 -1 8 10 
# 7
# 9 8 20 3 4 -1 0