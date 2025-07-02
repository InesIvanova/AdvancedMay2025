class Person:
    def __init__(self, age=0):
        self.age = age

    def sing(self):
        return 'singing...'

    def eat(self):
        self.sing()


p = Person(20)
print(p.age)