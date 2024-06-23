def dinhNghia(i):
    if i == 0: return 1
    if i == 1 or i == 2: return i
    if i == 3: return 6
    if i == 4: return 24
    if i == 5: return 120
    if i == 6: return 720
    if i == 7: return 5040
    if i == 8: return 40320
    if i == 9: return 363880

def fn(n):
    tong = 0
    for i in n:
        tong += dinhNghia(int(i))
    return tong

for _ in range(int(input())):
    n = input()
    print('Yes' if int(n) == fn(n) else 'No')

# 2
# 145
# 235
