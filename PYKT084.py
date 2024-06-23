check = True
a = []
n = int(input())
cnt1, ac = 0, []
for i in range(n):
    x = input()
    if check:
        ac.append(x)
        check = False
        continue
    if x == '':
        check = True
        ac.append(cnt1)
        a.append(ac)
        # print(*ac)
        ac = [] # dung dung clear o day!!
        cnt1 = 0
        continue
    cnt1 += 1
    if i == n - 1:
        ac.append(cnt1)
        a.append(ac)
        # print(*ac)
for i in range(len(a)): print(f'{a[i][0]}: {a[i][1]}')

# 8
# Home / accommodation
# What kind of housing / accommodation do you live in?
# Who do you live with?
# How long have you lived there?
#
# Study
# What is your area of specialization?
# Why did you choose to study that major?