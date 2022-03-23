from tkinter import N


rem = lambda num: num % 2

print(rem(5))

pro = lambda x, y: x * y
print(pro(2, 3))


def testf(num):

    print(num)
    return lambda x: x * num


res10 = testf(10)
res100 = testf(100)

print(res10)
print(res100)

print(res100(9))


def testf2(n):

    return lambda a: a * n


mydbl = testf2(2)
mytrpl = testf2(3)

print(mydbl(11))
print(mytrpl(11))


nlist = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

flist = list(filter(lambda num: (num > 7), nlist))

print(flist)


def add(n):
    return n + n


numbers = [1, 2, 3, 4]
result = map(add, numbers)
print(list(result))

result = list(map(lambda n: n + n, numbers))
print(result)

import os

clear = lambda: os.system("cls")
clear()
