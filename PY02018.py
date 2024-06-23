check = False
n = int(input())
a = sorted(list(map(int, input().split())))
# print(a)
for i in range(1, len(a)):
    if a[i] != a[i - 1] + 1:
        check = True
        print(a[i - 1] + 1)
        break
if not check: print(a[n - 1] + 1)