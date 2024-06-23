fi = [1] * 94
def dn():
    global fi
    for i in range(3, 94): fi[i] = fi[i - 1] + fi[i - 2]

dn()
for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(fi[i] , end = ' ')
    print()