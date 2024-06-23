class sophuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def tich(self, other):
        kq = sophuc(0, 0)
        kq.thuc = self.thuc * other.thuc - self.ao * other.ao
        kq.ao = self.thuc * other.ao + self.ao * other.thuc
        return kq

    def tong(self, other):
        kq = sophuc(0, 0)
        kq.thuc = self.thuc + other.thuc
        kq.ao = self.ao + other.ao
        return kq

    def __str__(self):
        return '{} + {}i'.format(self.thuc, self.ao)


for _ in range(int(input())):
    ab = list(map(int, input().split()))
    a = sophuc(ab[0], ab[1])
    b = sophuc(ab[2], ab[3])
    c = (a.tong(b)).tich(a)
    dc = (a.tong(b))
    d = dc.tich(dc)
    print(f'{c}, {d}')


# 3
# 1 2 3 4
# 2 3 4 5
# 1 -2 5 -6
