from audioop import mul


x = [i for i in range(10)]
print(x)

squares = [i ** 2 for i in range(10)]
print(squares)

list1 = [3, 4, 5]
mult = [item * 3 for item in list1]
print(mult)

wlist = ["this", "is", "a", "list", "of", "words"]
first = [word[0] for word in wlist]
print(first)

list2 = ["A", "B", "C"]
lower = [x.lower() for x in list2]
print(lower)

new_range = [i * i for i in range(5) if i % 2 == 0]
print(new_range)

string = "Hello 12345 World"

myf = open("test.txt", "r")
result = [i for i in myf if "line3" in i]
print(result)


def double(x):
    return x * 2


print(double(10))

myn = [double(x) for x in range(10)]
print(myn)

myn = [double(x) for x in range(10) if x % 2 == 0]
print(myn)

result = [x + y for x in [10, 30, 50] for y in [20, 40, 60]]
print(result)
