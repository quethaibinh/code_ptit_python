def dinhNghia(n, t):
    if (t == 3 and n >= 21) or (t == 4 and n <= 19): return 'Bach Duong'
    if (t == 4 and n >= 20) or (t == 5 and n <= 20): return 'Kim Nguu'
    if (t == 5 and n >= 21) or (t == 6 and n <= 20): return 'Song Tu'
    if (t == 6 and n >= 21) or (t == 7 and n <= 22): return 'Cu Giai'
    if (t == 7 and n >= 23) or (t == 8 and n <= 22): return 'Su Tu'
    if (t == 8 and n >= 23) or (t == 9 and n <= 22): return 'Xu Nu'
    if (t == 9 and n >= 23) or (t == 10 and n <= 22): return 'Thien Binh'
    if (t == 10 and n >= 23) or (t == 11 and n <= 22): return 'Thien Yet'
    if (t == 11 and n >= 23) or (t == 12 and n <= 21): return 'Nhan Ma'
    if (t == 12 and n >= 22) or (t == 1 and n <= 19): return 'Ma Ket'
    if (t == 1 and n >= 20) or (t == 2 and n <= 18): return 'Bao Binh'
    if (t == 2 and n >= 19) or (t == 3 and n <= 20): return 'Song Ngu'

for _ in range(int(input())):
    n, t = map(int, input().split())
    print(dinhNghia(n, t))

# 2
# 5 5
# 30 7