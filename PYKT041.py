n = int(input())
a, cnt = [], 0
for i in range(n):
    a.append(input())
for i in range(n):
    cntc = 0
    for j in range(n):
        if a[i][j] == 'C':cntc += 1
    cnt += (cntc * (cntc - 1)) // 2
for i in range(n):
    cntc = 0
    for j in range(n):
        if a[j][i] == 'C': cntc += 1
    cnt += (cntc * (cntc - 1)) // 2
print(cnt)

# 4
# CC..
# C..C
# .CC.
# .CC.