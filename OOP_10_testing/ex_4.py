class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class CarTests(TestCase):
    def test_make_empty_or_none_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("", "test", 5, 40)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car(None, "test", 5, 40)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_empty_or_none_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("test", "", 5, 40)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("test", None, 5, 40)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_zero_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("test", "test", 0, 40)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("test", "test", -1, 40)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_zero_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            Car("test", "test", 5, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("test", "test", 5, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_init(self):
        car = Car("test", "test model", 5, 40)
        self.assertEqual("test", car.make)
        self.assertEqual("test model", car.model)
        self.assertEqual(5, car.fuel_consumption)
        self.assertEqual(40, car.fuel_capacity)
        self.assertEqual( 0, car.fuel_amount)

    def test_fuel_amount_negative_raises(self):
        car = Car("test", "test model", 5, 40)
        self.assertEqual(car.fuel_amount, 0)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -10

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_zero_or_less_raises(self):
        car = Car("test", "test model", 5, 40)
        self.assertEqual( 0, car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        self.assertEqual( 0, car.fuel_amount)

    def test_refuel(self):
        car = Car("test", "test model", 5, 40)
        self.assertEqual( 0, car.fuel_amount)

        car.refuel(10)
        self.assertEqual(10, car.fuel_amount)

    def test_refuel_above_capacity(self):
        car = Car("test", "test model", 5, 40)
        self.assertEqual(0, car.fuel_amount)

        car.refuel(41)
        self.assertEqual(40, car.fuel_amount)

    def test_drive_not_enough_fuel_raises(self):
        car = Car("test", "test model", 5, 40)
        car.fuel_amount = 2
        self.assertEqual(2, car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            car.drive(400)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_at_capacity(self):
        car = Car("test", "test model", 5, 40)
        car.fuel_amount = 20
        car.drive(400)
        self.assertEqual(0, car.fuel_amount)

    def test_drive(self):
        car = Car("test", "test model", 5, 40)
        car.fuel_amount = 21
        car.drive(400)
        self.assertEqual(1, car.fuel_amount)



if __name__ == '__main__':
    main()