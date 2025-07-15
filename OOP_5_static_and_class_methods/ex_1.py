from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)

print(Calculator.add(1, 2))