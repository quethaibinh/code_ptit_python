from math import *
def check(a):
    if a == 0 or a == 1: return False
    for i in range(2, isqrt(a) + 1):
        if a % i == 0: return False
    return True

n = int(input())
a = list(map(int, input().split()))
dic = {}
for i in range(len(a)):
    if check(a[i]):
        if a[i] in dic:
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1
for i in dic:
    print(i, dic[i])

# 10
# 2 4 7 5 7 8 9 3 7 2