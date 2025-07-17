# class first_n_iterator:
#     def __init__(self, end):
#         self.current = -1
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current += 1
#         if self.current >= self.end:
#             raise StopIteration
#         return self.current
#
#
# my_obj = first_n_iterator(5)
# for num in my_obj:
#     print(num)
#
#
# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
#
# my_obj_gen = first_n(5)
# for num in my_obj_gen:
#     print(num)
#


def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


result = my_gen()

my_list = [1, 3, 6, 10]

result = (x**2 for x in my_list)
for el in result:
    print(el)
