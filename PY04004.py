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
        return p

def sum(p1, p2):
    p3 = PhanSo(0, 0)
    p1 = p1.rutgon()
    p2 = p2.rutgon()
    LCM = (p1.mau * p2.mau) // gcd(p1.mau, p2.mau)
    p3.tu = (p1.tu * (LCM // p1.mau)) + (p2.tu * (LCM // p2.mau))
    p3.mau = LCM
    p3 = p3.rutgon()
    return '{}/{}'.format(p3.tu, p3.mau)

arr = list(map(int, input().split()))
p1 = PhanSo(arr[0], arr[1])
p2 = PhanSo(arr[2], arr[3])
print(sum(p1, p2))