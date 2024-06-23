def check(s):
    if len(s) == 0 or len(s) == 1: return False
    cnt = 0
    for i in range(len(s)):
        if s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i] == '7': cnt += 1
    if cnt <= (len(s) // 2) : return False
    for i in range(2, len(s)):
        if len(s) % i == 0: return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')

# 3
# 1234567
# 22334455667
# 23400300489898989