class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.chuyen_can = 10
        self.trang_thai = ''

    def __str__(self):
        if self.chuyen_can <= 0: return '{} {} {} 0 KDDK'.format(self.ma, self.ten, self.lop)
        return '{} {} {} {}'.format(self.ma, self.ten, self.lop, self.chuyen_can)

class DiHoc:
    def __init__(self, ma, tinh_trang):
        self.ma = ma
        self.tinh_trang = tinh_trang

def check(a, b):
    for i in a:
        for j in b:
            if i.ma == j.ma:
                for k in j.tinh_trang:
                    if k == 'v': i.chuyen_can -= 2
                    if k == 'm': i.chuyen_can -= 1
                break

a, b = [], []
n = int(input())
for i in range(n):
    a.append(SinhVien(input(), input(), input()))
for i in range(n):
    ma, tt = input().split()
    b.append(DiHoc(ma, tt))
check(a, b)

for i in a: print(i)

# 3
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm