for _ in range(int(input())):
    s = input()
    a = s
    # print(len(s))
    if len(s) > 100:
        a = s[:100]
        if s[100] != ' ':
            # print(s[100])
            i = 99
            while s[i] != ' ':
                i -= 1
            a = s[:i]
    print(a)

# 2
# thanh Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021
# Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen