class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start-1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.end:
            self.current = self.start - 1
            raise StopIteration
        return self.current

iter_obj = filter(lambda x: x %2 ==0, [1, 2, 3, 4])

my_custom_range = custom_range(1, 5)
for item in my_custom_range:
    print(item)

for item in my_custom_range:
    print(item)

#
# for num in iter_obj:
#     print(num)
#
# for num in iter_obj:
#     print(num)