class matran:
    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt
        self.mtkq = [];
        for i in range(self.n):
            self.mtkq += [[0] * self.n]
            for j in range(self.n):
                for k in range(self.m):
                    self.mtkq[i][j] += (self.mt[i][k] * self.mt[j][k])

    def __str__(self):
        for i in self.mtkq:
            print(*i)
        return ''

for _ in range(int(input())):
    n, m = map(int, input().split())
    mt = []
    for i in range(n):
        mt.append(list(map(int, input().split())))
    # for i in mt:
    #     print(*i)
    print(matran(n, m, mt))


# 1
# 2  2
# 1  2
# 3  4