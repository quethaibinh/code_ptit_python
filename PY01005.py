s = input()
cnt4 = 0
cnt7 = 0
for i in s:
    if int(i) == 4:
        cnt4 += 1
    if int(i) == 7:
        cnt7 += 1
cnt = cnt4 + cnt7
if cnt == 4 or cnt == 7: print('YES')
else: print('NO')