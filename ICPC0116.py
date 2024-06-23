def inkq(n):
    print('YES' if n[:1] == n[-1:] else 'NO')
for _ in range(int(input())):
    inkq(input())

# 2
# 12345
# 123451