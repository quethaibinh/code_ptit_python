class Gamer:
    def __init__(self, ma, ten, time_in, time_out):
        self.ma = ma
        self.ten = ten
        self.time_in = time_in
        self.time_out = time_out
        self.gio_vao, self.phut_vao = map(int, time_in.split(':'))
        self.gio_ra, self.phut_ra = map(int, time_out.split(':'))
        self.thoi_gian_choi =self.gio_ra * 60 + self.phut_ra -  self.gio_vao * 60 - self.phut_vao

    def __str__(self):
        return '{} {} {} gio {} phut'.format(self.ma, self.ten, self.thoi_gian_choi // 60, self.thoi_gian_choi % 60)

a = []
for _ in range(int(input())):
    a.append(Gamer(input(), input(), input(), input()))
a.sort(key = lambda x : - x.thoi_gian_choi)
for i in a: print(i)


# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00