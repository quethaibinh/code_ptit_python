s = input()
used = [1] * len(s)

def tryy(s1):
    global used
    if len(s1) == len(s):
        print(s1)
    for j in range(len(s)):
        if used[j] == 1:
            used[j] = 0
            tryy(s1 + s[j])
            used[j] = 1
tryy('')