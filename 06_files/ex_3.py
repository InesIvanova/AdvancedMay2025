import os

from constants import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, "lab_files", "ex_3", "my_first_file.txt")

with open(path, "w") as file:
    file.write("I just created my first file!")