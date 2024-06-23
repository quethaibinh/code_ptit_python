def check(a):
    if a != a[::-1]:
        return False
    for i in a:
        if int(i) % 2 != 0:
            return False
    return True

for t in range(int(input())):
    for i in range(22, int(input()), 2):
        if(check(str(i)) and int(len(str(i))) % 2 == 0):
            print(i, end=' ')
    print()