def check(s):
    if len(s) % 2 == 0: return False
    if s[0] == s[1]: return False
    for i in range(2, len(s), 2):
        if s[i] != s[0]: return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')

# 2
# 2324272921262
# 13141516