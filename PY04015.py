t = 1
class TienNuoc:
    def __init__(self, ten, trc, sau):
        global t
        self.ten = ten
        self.trc = trc
        self.sau = sau
        self.so_nuoc_dung = self.sau - self.trc
        if self.so_nuoc_dung <= 50: self.tien = self.so_nuoc_dung * 100 + (self.so_nuoc_dung * 100 ) * 0.02
        elif self.so_nuoc_dung <= 100: self.tien = 50 * 100 + (self.so_nuoc_dung - 50) * 150 + (50 * 100 + (self.so_nuoc_dung - 50) * 150) * 0.03
        else: self.tien = 50 * 100 + 50 * 150 + (self.so_nuoc_dung - 100) * 200 + (50 * 100 + 50 * 150 + (self.so_nuoc_dung - 100) * 200) * 0.05
        if t // 10 == 0: self.ma = 'KH0' + str(t)
        else: self.ma = 'KH' + str(t)
        t += 1

    def __str__(self):
        return '{} {} {}'.format(self.ma, self.ten, round(self.tien))

a = []
for _ in range(int(input())):
    a.append(TienNuoc(input(), int(input()), int(input())))
a.sort(key = lambda x : - x.tien)
for i in range(len(a)):
    print(a[i])

# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 160
# Ha Hue Anh
# 410
# 612