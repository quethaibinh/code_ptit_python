def chuan_hoa(s):
    return s.capitalize()
class SinhVien:
    def __init__(self, ma, ten, ns, d1, d2, d3):
        self.ma = ma
        self.ten = ten
        self.ns = ns
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.tong_diem = (self.d1 + self.d2 + self.d3) / 3
        self.thu_hang = 0

    def __str__(self):
        if self.ns[2] != '/': self.ns = '0' + self.ns
        x = self.ns
        if self.ns[5] != '/': self.ns = x[:3] + '0' + x[-6:]
        s = list(self.ten.split())
        sc = ''
        for i in s: sc += chuan_hoa(i) + ' '
        self.ten = sc
        return '{} {} {}{} {}'.format(self.thu_hang, self.ma, self.ten, self.ns, '{:.2f}'.format(self.tong_diem))

a = []
for _ in range(int(input())):
    a.append(SinhVien(input(), input(), input(), float(input()), float(input()), float(input())))
a.sort(key = lambda x : - x.tong_diem)
check = a[0].tong_diem
cnt = 1
cntc = 1
a[0].thu_hang = 1
for i in range(1, len(a)):
    if a[i].tong_diem == check:
        a[i].thu_hang = cnt
        cntc += 1
    else:
        cnt += cntc
        a[i].thu_hang = cnt
        cntc = 1
    check = a[i].tong_diem
for i in range(len(a)):
    min_pos = i
    for j in range(i + 1, len(a)):
        if a[min_pos].thu_hang == a[j].thu_hang and a[j].ma < a[min_pos].ma: j = min_pos
    tmp = a[i]
    a[i] = a[min_pos]
    a[min_pos] = tmp
for i in a: print(i)