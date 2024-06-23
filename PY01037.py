from math import *
dic = {}
def dn():
    for i in range(1, 10000001):
        dic[i] = 0
    for i in range(1, int(sqrt(10000000))):
        for j in range(i, 10000001, i):
            dic[i] += 1

for _ in range(int(input())):
    dn()
    n = int(input())
    check = True
    for i in range(n + 1, 10000001):
        for j in range(1, i + 1):
            if dic[i] <= dic[j]:
                check = False
                break
        if check:
            print(i)
            break

