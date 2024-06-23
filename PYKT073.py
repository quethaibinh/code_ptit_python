n = int(input())
a, b = [], []
for i in range(n):
    a.append(list(map(str, input().split())))
i = 0
while i < n:
    x = len(a[i])
    if x == 6 or x == 8:
        b.append(1)
        while i < n and (len(a[i]) == 6 or len(a[i]) == 8): i += 1
    else:
        b.append(2)
        i += 4
print(len(b))
for j in range(len(b)): print(b[j])

# 8
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon