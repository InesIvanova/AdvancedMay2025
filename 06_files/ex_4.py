import os

from constants import ABSOLUTE_PROJECT_PATH


try:
    path = os.path.join(ABSOLUTE_PROJECT_PATH, "lab_files", "ex_3", "my_first_file.txt")
    os.remove(path)
except FileNotFoundError:
    print("File already deleted")