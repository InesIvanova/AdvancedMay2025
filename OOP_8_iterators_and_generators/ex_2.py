class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current_index = len(self.iterable)
        self.reversed_iterator = reversed(self.iterable)

    def __iter__(self):
        return self.reversed_iterator

    # def __next__(self):
    #     self.current_index -= 1
    #     if self.current_index < 0:
    #         raise StopIteration
    #     return self.iterable[self.current_index]



reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
