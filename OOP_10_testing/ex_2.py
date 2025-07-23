class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def test_init(self):
        cat = Cat('Tom')
        self.assertEqual('Tom', cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_eat_already_fet_raises(self):
        cat = Cat('Tom')
        cat.fed = True

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

        self.assertEqual(0, cat.size)
        self.assertTrue(cat.fed)
        self.assertFalse(cat.sleepy)

    def test_eat(self):
        cat = Cat('Tom')

        cat.eat()

        self.assertEqual(1, cat.size)
        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)

        cat.fed = False

        cat.eat()
        self.assertEqual(2, cat.size)
        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)

    def test_sleep_cat_not_fed_raises(self):
        cat = Cat('Tom')

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

        self.assertFalse(cat.sleepy)

    def test_sleep(self):
        cat = Cat('Tom')

        cat.eat()
        self.assertTrue(cat.sleepy)
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    main()