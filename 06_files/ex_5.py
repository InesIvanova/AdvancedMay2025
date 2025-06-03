import os
import re

from constants import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, "lab_files", "ex_5")

with open(os.path.join(path, "input.txt")) as file:
    text = file.read()

with open(os.path.join(path, "words.txt")) as file:
    words = file.read().split()


print("all files read")
data = {}

for word in words:
    pattern = rf"\b{word}\b"
    count = len(re.findall(pattern, text, re.IGNORECASE))
    data[word] = count

sorted_data = sorted(data.items(), key=lambda kvp: -kvp[1])

with open(os.path.join(path, "output.txt"), "w") as file:
    for key, value in sorted_data:
        file.write(f"{key} - {value}\n")