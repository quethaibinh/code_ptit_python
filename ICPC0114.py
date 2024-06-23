from math import *
# a = [1] * 10000007
def a(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def check(n):
    b = n[::-1]
    if a(int(n)) != 1 or a(int(b)) != 1: return False
    sum = 0
    for i in n:
        if i != '2' and i != '3' and i != '5' and i != '7': return False
        sum += int(i)
    if a(sum): return True
    return False

for _ in range(int(input())):
    print('Yes' if check(input()) else 'No')

# 3
# 13
# 753
# 757