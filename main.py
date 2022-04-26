def task_1():
    s = '7' * 2022
    while '777' in s or '333' in s:
        s = s.replace('777', '3', 1)
        s = s.replace('333', '7', 1)
    print(s)


# task_1()
def task_2():
    def f(x, y, z, w):
        return (x <= y) and ((not x) <= (not z)) or w

    print('x y z w')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if f(x, y, z, w) == 0:
                        print(x, y, z, w)


# task_2()

def task_4():
    x = 0
    while True:
        x += 1
        x2 = bin(x)[2:]
        if x % 2 == 0:
            x2 += '10'
        else:
            x2 += '11'

        if x2.count('1') % 2 == 0:
            x2 += '0'
        else:
            x2 += '1'
        res = int(x2, 2)
        if res > 53:
            print(x)
            break


# print(int('111', 2))
# task_4()

def task_5():
    s = 0
    while True:
        s += 1
        sc = s
        n = 200
        while sc > 0:
            sc = sc // 4
            n = n - 6
        if n == 170:
            print(s)
            break


# task_5()

def task_10():
    def to4(x):
        res = ''
        while x > 0:
            res += str(x % 4)
            x //= 4
        return res[::-1]

    s = 16 ** 23 + 4 ** 12 - 32 ** 6
    print(to4(s).count('3'))


# task_10()
def task_11():
    def f(x, y):
        if x == y:
            return 1
        elif x > y or x == 24:
            return 0
        else:
            return f(x + 1, y) + f(3 * x, y)

    print(f(2, 12) * f(12, 72))


# task_11()


def task_12():
    x = 0
    while True:
        x += 1
        xc = x
        L = 0
        M = 0
        while xc > 0:
            L = L + 1
            if M < (xc % 8):
                M = xc % 8
            xc = xc // 8
        if L == 4 and M == 7:
            print(x)
            break


# task_12()
def task_13():
    def deli(x, t):
        return not(x % t)

    def f(x, A):
        return (not deli(x, 54) or not deli(x, 80)) <= (not deli(x, A))

    A = 0
    while True:
        A += 1
        for x in range(1, 100001):
            if f(x, A) == False:
                break
        else:
            print(A)
            break

# task_13()

def task_14():
    data = list(map(int, open('14.txt').read().splitlines()))
    count = 0
    max_sum = 0
    for i in range(len(data)-1):
        if data[i]%4 == 0 and data[i+1]%4 == 0:
            count += 1
            max_sum = max(max_sum, data[i]+data[i+1])
    print(count, max_sum)

task_14()







