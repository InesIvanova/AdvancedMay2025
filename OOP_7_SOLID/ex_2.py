from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Frog(Animal):
    def make_sound(self):
        return "frog sound"


class Pig(Animal):
    def make_sound(self):
        return "pig sound"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Frog(), Pig()]
animal_sound(animals)

