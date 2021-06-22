def mult(a, b):
    if a < 11:
        return a * b
    else:
        return b


def sumsquare(a, b):
    print("the sum of squares is {}".format(a ** 2 + b ** 2))


print(mult(10, 5.5))
sumsquare(1.5, 7.8)


def squaresum(x, y):
    if x > 0:
        return x ** 2 + y ** 2


# anonymous function: lambda function
# syntax: lambda arguments: expression
f = lambda x, y: x ** 2 + y ** 2
f1 = lambda x, y: x ** 2 + y ** 2 if (x > 0) else None

# print(type(f))
# print(squaresum(-1.5, 8.3))
# print(f1(-1.5, 8.3))

Max = lambda a, b: a if (a > b) else b

# print(Max(5, 10))

ages = [10, 90, 45, 70, 25, 32, 11, 78, 56, 8, 3]


def filter_condition(age):
    return age > 45


# print(filter_condition(46), filter_condition(12))

filtered_list = list(filter(lambda age: age > 45, ages))
# print(filtered_list)

def power(n):
    return lambda a: a**n

power1 = power(1)(10) # lambda a: a**1
power2 = power(2) # lambda a: a**2
power4 = power(4) # lambda a: a**4

num = 10

print(type(power1))
# print(power1(num))
print(power2(num))
print(power4(num))



