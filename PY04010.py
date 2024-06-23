class SinhVien:
    def __init__(self, ten, ns, d1, d2, d3):
        self.ten = ten
        self.ns = ns
        self.d1, self.d2, self.d3 = d1, d2, d3
        self.tong = self.d1 + self.d2 + self.d3

    def __str__(self):
        return '{} {} {}'.format(self.ten, self.ns, "{:.1f}".format(self.tong))

print(SinhVien(input(), input(), float(input()), float(input()), float(input())))

# Nguyen Hoang Ha
# 11/10/2001
# 4.5
# 10.0
# 5.5