n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in range(1, len(a)):
    if len(b) != 0:
        if (b[len(b) - 1] + a[i]) % 2 == 0: b.pop()
        else: b.append(a[i])
    else: b.append(a[i])
print(len(b)) 

# 10
# 1 5 5 8 6 4 3 5 9 3

# 5
# 2 3 4 5 6