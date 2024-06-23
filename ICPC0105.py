if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        s += 'z'
        s1 = 0
        maxx = 0
        for j in s:
            if j.isdigit():
                s1 = s1 * 10 + int(j)
            else:
                maxx = max(maxx, s1)
                s1 = 0
        print(maxx)