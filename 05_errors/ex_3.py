class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative("Please enter a positive number.")