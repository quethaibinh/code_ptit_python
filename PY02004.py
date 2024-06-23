n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(1, n):
    if(a[i] != a[i - 1]): cnt += 1
print(cnt)

# 6
# 1 0 0 1 1 1