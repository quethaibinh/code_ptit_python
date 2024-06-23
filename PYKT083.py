def init(s, n):
    if s == 'Xe_con':
        if n == '5': return 10000
        else: return 15000
    elif s == 'Xe_tai': return 20000
    else:
        if n == '29': return 50000
        else: return 70000

n = int(input())
a = []
dic = {}
for i in range(n):
    a.append(list(map(str, input().split())))
    if a[i][4] in dic and a[i][3] == 'IN': dic[a[i][4]] += init(a[i][1], a[i][2])
    elif a[i][3] == 'IN': dic[a[i][4]] = init(a[i][1], a[i][2])
for i in dic:
    print(f'{i}: {dic[i]}')

# 5
# 30F-123.15 Xe_con 5 OUT 06/11/2021
# 30F-123.15 Xe_con 5 IN 06/11/2021
# 30H-123.15 Xe_con 7 IN 06/11/2021
# 29H-222.68 Xe_tai 2 IN 07/11/2021
# 30G-511.15 Xe_con 5 IN 07/11/2021