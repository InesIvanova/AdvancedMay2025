class vowels:
    def __init__(self, text):
        self.text = text
        self.index = -1
        # self.vowels = [el for el in self.text if el.lower() in 'aeiouy']

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.text):
            raise StopIteration
        if self.text[self.index].lower() in 'aeiouy':
            return self.text[self.index]
        return self.__next__()
        # self.index += 1
        # if self.index >= len(self.vowels):
        #     raise StopIteration
        # return self.vowels[self.index]

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
