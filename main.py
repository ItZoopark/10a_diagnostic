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

task_5()
