def uoc(a, b):
    if b == 0: return a
    return uoc(b, a % b)

def check(a):
    if a == 0 or a == 1: return False
    for i in range(2, a, 1):
        if a % i == 0: return False
    return True

# if __name__ == '__main__':
for t in range(int(input())):
    n = int(input())
    cnt = 0
    a = []
    for i in range(1, n, 1):
        if uoc(n, i) == 1:
            cnt += 1
    # print(cnt)
    if check(cnt): print('YES')
    else: print('NO')