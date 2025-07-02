class Stack:
    def __init__(self, *args):
        self.data = []

        for el in args:
            if isinstance(el, str):
                self.data.append(el)

    def push(self, el):
        if isinstance(el, str):
            self.data.append(el)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        result = reversed(self.data)
        return f"[{', '.join(result)}]"


s = Stack("a", "b", "c")
print(s)
s.push("d")
print(s)
print(s.top())
print(s)
print(s.pop())
print(s)
print(s.is_empty())
print(s.pop())

print(s.pop())

print(s.pop())
print(s.is_empty())


