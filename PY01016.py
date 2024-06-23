for _ in range(int(input())):
    s = input()
    s2 = []
    for i in range(len(s)):
        if s[i].isdigit():
            for _ in range(int(s[i])):
                print(s[i - 1], end = '')
    print()

# 2
# A8
# A2E1C4G3D1