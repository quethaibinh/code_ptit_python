from math import *
def sum(a):
    tong = 0
    for i in range(2, isqrt(a) + 1):
        if int(a) % i == 0:
            while int(a) % i == 0:
                tong += i
                a //= i
    if a != 1: tong += a
    return tong

tong = 0
list1 = []
list2 = []
for _ in range(int(input())):
    a = int(input())
    list1.append(a)
for j in range(len(list1)):
    i = list1[j]
    sum1 = 0
    k = 0
    while k < j:
        if i % list1[k] == 0:
            sum1 += list2[k]
            i //= list1[k]
        k += 1
    if i != 1: sum1 += sum(i)
    list2.append(sum1)
for i in list2:
    tong += i
print(tong)

# 5
# 7
# 9
# 10
# 13
# 100