from math import *
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        p = PhanSo(0, 0)
        GCD = gcd(self.tu, self.mau)
        p.tu = self.tu // GCD
        p.mau = self.mau // GCD
        return '{}/{}'.format(p.tu, p.mau)
x, y = map(int, input().split())
p = PhanSo(x, y)
print(p.rutgon())