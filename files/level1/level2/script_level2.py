import os

path = os.path.join("..", "another_level_2", "nested_dir", "some_file.txt")
file = open(path)
print(file.read())


";".join(["a", "b"])