class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main

class WorkerTests(TestCase):
    def test_init_worker(self):
        worker = Worker("Test", 1000,100)

        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_work_negative_energy_raises(self):
        # Arrange
        worker = Worker("Test", 1000, -1)

        self.assertEqual(0, worker.money)
        self.assertEqual(-1, worker.energy)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

        self.assertEqual(0, worker.money)
        self.assertEqual(-1, worker.energy)

    def test_work_zero_energy_raises(self):
        # Arrange
        worker = Worker("Test", 1000, 0)

        self.assertEqual(0, worker.money)
        self.assertEqual(0, worker.energy)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual(0, worker.money)
        self.assertEqual(0, worker.energy)

    def test_work_earns_money(self):
        worker = Worker("Test", 1000, 100)

        self.assertEqual(0, worker.money)
        self.assertEqual(100, worker.energy)

        worker.work()
        worker.work()

        self.assertEqual(2000, worker.money)
        self.assertEqual(98, worker.energy)

    def test_rest(self):
        worker = Worker("Test", 1000, 100)

        self.assertEqual(100, worker.energy)

        worker.rest()
        worker.rest()

        self.assertEqual(102, worker.energy)

    def test_get_info(self):
        worker = Worker("Test", 1000, 100)
        self.assertEqual(0, worker.money)

        expected_result = "Test has saved 0 money."
        result = worker.get_info()
        self.assertEqual(expected_result, result)

        worker.work()
        worker.work()

        expected_result = "Test has saved 2000 money."
        result = worker.get_info()
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()