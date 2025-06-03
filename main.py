import os

from constants import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, "files", "example_down3.txt")

with open(path, "r") as file:
    print(file.read().split("\n"))
    print(file.closed)

print(file.closed)
