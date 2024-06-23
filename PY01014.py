a, k, n = map(int, input().split())
check = False
st = k - (a % k)
s = []
while a + st <= n:
    check = True
    s.append(st)
    st += k
if not check: print('-1')
else:
    for i in s:
        print(i, end = ' ')