se = set()
cnt = 0
while True:
    if cnt == 10: break
    b = list(map(int, input().split()))
    for i in range(len(b)):
        se.add(b[i] % 42)
        cnt += 1
print(len(se))