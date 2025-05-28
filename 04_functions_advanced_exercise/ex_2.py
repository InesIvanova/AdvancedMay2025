def kwargs_length(**kwargs) -> int:
    return len(kwargs)


print(kwargs_length(tonw="Petrich", age=20, color="red"))
print(kwargs_length())
print(kwargs_length(name="Test"))


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
print(kwargs_length(name="Peter", age=25))
