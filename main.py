class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.getter  # Redefine the getter for 'value'
    def value(self):
        print("Getting the value")
        return self._value * 2  # Modify the returned value


obj = MyClass(10)
print(obj.value)