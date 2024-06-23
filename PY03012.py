n = int(input())
a = []
for i in range(n):
    ac = []
    ac.append(input())
    c, su = map(int, input().split())
    ac.append(c)
    ac.append(su)
    a.append(ac)
for i in range(n):
    min_pos = i
    for j in range(i + 1, n):
        if a[j][1] == a[min_pos][1] and a[j][2] == a[min_pos][2] and a[j][0] < a[min_pos][0]: min_pos = j
        if a[j][1] == a[min_pos][1] and a[j][2] < a[min_pos][2]: min_pos = j
        if a[j][1] > a[min_pos][1]: min_pos = j
    x = a[i]
    a[i] = a[min_pos]
    a[min_pos] = x
for i in range(n):
    print(*a[i])

# 2
# Tran Thi Ngoc
# 168 600
# Nguyen Van Nam
# 168 601