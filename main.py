from abc import abstractmethod, ABC


class Person(ABC):
    MIN_AGE = 0
    MAX_AGE = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= self.MIN_AGE:
            raise ValueError("age must be positive")
        self.__age = value

    @abstractmethod
    def greet(self):
        pass


class Employee(Person):
    MIN_AGE = 16

    def greet(self):
        print("Employee {}".format(self.name))
