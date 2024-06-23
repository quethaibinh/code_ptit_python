s = input()
cntt = 0
cnth = 0
for i in s:
    if i.islower(): cntt += 1
    else: cnth += 1
if cntt >= cnth: print(s.lower())
else: print(s.upper())