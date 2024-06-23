t = 1
class NhanVien:
    def check(self):
        if self.lt > 10: self.lt /= 10
        if self.th > 10: self.th /= 10

    def __init__(self, ten, lt, th):
        global t
        self.ma = 'TS0' + str(t)
        # self.ma = 'TS' + str(t).zfill(2)
        t += 1
        self.ten = ten
        self.lt = lt
        self.th = th
        self.check()
        self.tb = (self.lt + self.th) / 2
        if self.tb < 5: self.trang_thai = 'TRUOT'
        elif self.tb < 8: self.trang_thai = 'CAN NHAC'
        elif self.tb < 9.5: self.trang_thai = 'DAT'
        else: self.trang_thai = 'XUAT SAC'

    def __str__(self):
        return '{} {} {} {}'.format(self.ma, self.ten, '{:.2f}'.format(self.tb), self.trang_thai)

a = []
for _ in range(int(input())):
    a.append(NhanVien(input(), float(input()), float(input())))
a.sort(key = lambda x : - x.tb)
for i in a:
    print(i)


# 3
# Nguyen Thai Binh
# 45
# 55
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56