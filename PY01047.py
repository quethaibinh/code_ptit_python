from math import *
def check(a):
    if a == 0 or a == 1: return False
    for i in range(2, int(sqrt(a))):
        if a % i == 0: return False
    return True

for _ in range(int(input())):
    s = int(input()[-4:])
    print('YES' if check(s) else 'NO')

# 3
# 12234323130097
# 3443354654654654461123
# 43543543434554659999

# 3
# 12234323130097
# 3443354654654654461123
# 43543543434554659999