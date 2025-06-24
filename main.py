# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
#
#
#
# class Greeter:
#     def greet(self, person: Person):
#         print(f"Hi, {person.name}!")
#
#
# greeter = Greeter()
# person = Person("Test")
# greeter.greet(person)


class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        return f"the animal with name {self.name} is sleeping.."

    def eat(self):
        return f"the animal with name is eating."

animal = Animal("cat")
print(animal.name)
print(animal.sleep()) # sleeping..

