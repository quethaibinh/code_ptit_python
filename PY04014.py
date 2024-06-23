from decimal import ROUND_HALF_UP, Decimal
x = 1
class TongKet:
    def __init__(self, ten, a):
        global x
        self.ten = ten
        self.a = a
        self.tb = self.a[0] * 2 + self.a[1] *2
        for i in range(2, 10): self.tb += a[i]
        self.tb /= 12
        if self.tb < 5: self.xep_loai = 'YEU'
        elif self.tb < 7: self.xep_loai = 'TB'
        elif self.tb < 8: self.xep_loai = 'KHA'
        elif self.tb < 9: self.xep_loai = 'GIOI'
        else: self.xep_loai = 'XUAT SAC'
        if x // 10 == 0: self.ma = 'HS0' + str(x)
        else: self.ma = 'HS' + str(x)
        x += 1


    def __str__(self):
        return '{} {} {} {}'.format(self.ma, self.ten, self.tb.quantize(Decimal('0.1'), ROUND_HALF_UP), self.xep_loai)

a = []
for _ in range(int(input())):
    a.append(TongKet(input(), list(map(Decimal, input().split()))))
a.sort(key = lambda x : x.tb, reverse = True)
for i in range(len(a)):
    print(a[i])


# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0