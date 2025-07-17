def squares(n):
    start = 1
    while start <= n:
        yield start**2
        start += 1


for el in squares(5):
    print(el)
print(list(squares(5)))
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3])))