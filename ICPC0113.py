a = [1] * 1000007
def sang():
    a[0] = 0
    a[1] = 0
    for i in range(2, 1001):
        if a[i]:
            for j in range(i * i, 1000001, i):
                a[j] = 0
def check(a1, n):
    b = a1[::-1]
    if b == a1: return False
    if int(a1) > n or int(b) > n: return False
    if a[int(a1)] and a[int(b)]: return True
    return False

sang()
for _ in range(int(input())):
    s = []
    n = int(input())
    dic = {}
    for i in range(1, n):
        if check(str(i), n):
            s.append(i)
            dic[i] = 1
    for i in s:
        if dic[i]:
            s1 = str(i)
            s1 = s1[::-1]
            print(i, s1, end = ' ')
            dic[int(s1)] = 0
    print()

