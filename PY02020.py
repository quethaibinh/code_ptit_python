n = int(input())
a = sorted(list(map(float, input().split())))
minn, maxx = a[0], a[len(a) - 1]
res = 0.0
cnt = 0
for i in range(len(a)):
    if a[i] == maxx or a[i] == minn: continue
    else:
        res += a[i]
        cnt += 1
print("{:.2f}".format(res / cnt))

# 6
# 6.75 8 9.2 7.25 7.75 6.75
