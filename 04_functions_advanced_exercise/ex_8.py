def age_assignment(*args, **kwargs):
    data = {}
    for first_letter, age in kwargs.items():
        names = [name for name in args if name.startswith(first_letter)]
        for name in names:
            data[name] = age

    sorted_data = sorted(data.items(), key=lambda kvp: kvp[0])
    # sorted_data = sorted(data)
    # result = ""
    # for name in sorted_data:
    #     result += f"{name} is {sorted_data[name]} years old.\n"
    # return result

    result = ""
    for name, age in sorted_data:
        result += f"{name} is {age} years old.\n"
    return result

print(age_assignment("Peter", "George", G=26, P=19))