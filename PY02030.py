nt = [1] * 1000006
def sng():
    nt[0] = nt[1] = 0
    for i in range(2, 1001):
        if nt[i]:
            for j in range(i * i, 1000001, i):
                nt[j] = 0
sng()
n = int(input())
a = list(map(int, input().split()))
j = 0
check = False
dic = {}
tong = []
while j < len(a):
    if a[j] in dic: del a[j]
    else:
        dic[a[j]] = 1
        j += 1
for i in range(len(a)):
    if i == 0: tong.append(a[i])
    else: tong.append(tong[i - 1] + a[i])
for i in range(len(a)):
    if nt[tong[i]] and nt[tong[len(a) - 1] - tong[i]]:
        print(i)
        check = True
        break;
if not check: print('NOT FOUND')

# for i in range(len(a)):
#     print(a[i], end = ' ')

# 10
# 3 6 7 3 4 7 3 6 4 4

# 10
# 3 6 7 3 5 7 3 6 6 7