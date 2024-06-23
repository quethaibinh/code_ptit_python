from math import *
class Point:
    def __init__(self, hoanh, tung):
        self.hoanh = hoanh
        self.tung = tung
    def distance(self, p):
        x = self.hoanh - p.hoanh
        y = self.tung - p.tung
        return "{:.4f}".format(sqrt(x * x + y * y))
def Decimal(x):
    return float(x)

t = int(input())
while t > 0:
    arr = input().split()
    p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
    p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
    print(p1.distance(p2))
    t -= 1

# 2
# 0 0 0 5
# 0 199 5 6