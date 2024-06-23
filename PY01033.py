def uoc(a, b):
    if b == 0: return a
    else: return uoc(b, a % b)

a, b = map(int, input().split())
for i in range(a, b - 1):
    for j in range(i + 1, b):
        if uoc(i, j) == 1:
            for k in range(j + 1, b + 1):
                if uoc(j, k) == 1 and uoc(i, k) == 1:
                    print(f'({i}, {j}, {k})')
