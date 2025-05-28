def concatenate(*args, **kwargs):
    text = ''.join(args)

    for key, value in kwargs.items():
        text = text.replace(key, value)
    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))


def some_func(*args, **kwargs):
    pass
some_func(1, 2, 34, 4, 5, name="sofia")