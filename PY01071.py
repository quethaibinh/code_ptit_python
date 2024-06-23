def check(s):
    if len(s) >= 3 and s[-3:] == '.py': return True
    return False

print('yes' if check(input().lower()) else 'no')