import os

from constants import ABSOLUTE_PROJECT_PATH

# using relative path
# path = os.path.join("..", "lab_files", "ex_1", "text.txt")

# Using absolute path
path = os.path.join(ABSOLUTE_PROJECT_PATH, "lab_files", "ex_1", "text.txt")

try:
    open(path)
    print("File found")
except FileNotFoundError:
    print("File not found")