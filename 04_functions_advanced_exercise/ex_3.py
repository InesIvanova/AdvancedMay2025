from typing import Any


def even_odd(*args: Any) -> list[int]:
    nums = list(args)
    command = nums.pop()
    if command.lower() == 'even':
        return [el for el in nums if el % 2 == 0]
    else:
        return [el for el in nums if el % 2 != 0]




print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))