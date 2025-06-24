class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}."

car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())

import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        car = Car("W124", "Mercedes", "Petrol l4")
        self.assertEqual(car.name, "W124")
        self.assertEqual(car.model, "Mercedes")
        self.assertEqual(car.engine, "Petrol l4")

    def test_get_info(self):
        car = Car("W124", "Mercedes", "Petrol l4")
        self.assertEqual(car.get_info(), "This is W124 Mercedes with engine Petrol l4")


if __name__ == "__main__":
    unittest.main()
