import os

from constants import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, "lab_files", "ex_2", "numbers.txt")
file = open(path)

# numbers = [int(el) for el in file.read().split("\n")]
# print(sum(numbers))

total = 0
for el in file.readlines():
    # if el.endswith("\n"):
    #     el = el[:-1]
    total += int(el)

print(total)