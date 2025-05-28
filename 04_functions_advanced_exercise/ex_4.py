def even_odd_filter(**kwargs) -> dict[str, list[int]]:
    even = []
    odd = []
    for el in kwargs["odd"]:
        odd.append(el)

    if "odd" in kwargs:
        kwargs["odd"] = odd
    if "even" in kwargs:
        kwargs["even"] = [el for el in kwargs["even"] if el % 2 == 0]

    sorted_kwargs = sorted(kwargs.items(), key=lambda kvp: -len(kvp[1]))
    return dict(sorted_kwargs)


# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))

a = even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
)
b = 5


