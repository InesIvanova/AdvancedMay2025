def sum_nums(a, b):
    return a + b


def subtract_nums(a, b):
    return a - b

def multiply_nums(a, b):
    return a * b


def divide_nums(a, b):
    return a / b

def pow_nums(a, b):
    return a ** b


mapper = {
    "+": sum_nums,
    "-": subtract_nums,
    "*": multiply_nums,
    "/": divide_nums,
    "^": pow_nums,
}

def calculate(a, b, sign):
    return mapper[sign](a, b)




