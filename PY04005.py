from math import *
class Point:
    def __init__(self, hoanh, tung):
        self.hoanh = hoanh
        self.tung = tung
def DoDai(a1, a2):
    x = a1.hoanh - a2.hoanh
    y = a1.tung - a2.tung
    # return "{:.9f}".format(sqrt(x * x + y * y))
    # return sqrt(x * x + y * y)
    return round(sqrt(x * x + y * y), 12)

def check(a1, a2, a3):
    d1 = DoDai(a1, a2)
    d2 = DoDai(a2, a3)
    d3 = DoDai(a1, a3)
    # return max(d1, d2, d3)
    if max(d1, d2, d3) * 2 >= d1 + d2 + d3: return 'INVALID'
    return "{:.3f}".format(d1 + d2 + d3)
    # return round(d1 + d2 + d3, 3)

vector = []
for _ in range(int(input())):
    arr = list(map(float, input().split()))
    # print(*arr)
    cur_arr = []
    for i in range(0, 6, 2):
        cur_arr.append(Point(arr[i], arr[i + 1]))
    vector.append(cur_arr)

for i in range(len(vector)):
    print(check(vector[i][0], vector[i][1], vector[i][2]))

    # print(check(a1, a2, a3))

# 3
# 0 0 0 5 0 199
# 1 1 1 1 1 1
# 0 0 0 5 5 0