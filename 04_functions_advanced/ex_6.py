from functools import reduce
#
#
# def operate(operator, *args):
#     if operator == "+":
#         return reduce(lambda x, y: x + y, args)
#     elif operator == "*":
#         return reduce(lambda x, y: x * y, args)
#     elif operator == "/":
#         return reduce(lambda x, y: x / y, args)
#     elif operator == "-":
#         return reduce(lambda x, y: x - y, args)
#
# print(operate("+", 1, 2, 3))


def add(*args):
    return reduce(lambda x, y: x + y, args)

def subtract(*args):
    return reduce(lambda x, y: x - y, args)

def multiply(*args):
    return reduce(lambda x, y: x * y, args)

def divide(*args):
    return reduce(lambda x, y: x / y, args)


mapper = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def operate(operator, *args):
    return mapper[operator](*args)


print(operate("+", 1, 2, 3))