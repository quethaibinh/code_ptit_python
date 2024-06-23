t = int(input())
for z in range(t) :
    m = {}
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in a :
        if i in m : m[i] += 1
        else : m[i] = 1
    for i in m :
        if m[i] % 2 == 1 :
            print(i)
            break

# 2
# 7
# 1 2 3 2 3 1 3
# 5
# 1 1 3 3 2