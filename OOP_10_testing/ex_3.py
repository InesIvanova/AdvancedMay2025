class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.integerList = IntegerList(4, 3, 6)

    def test_init_allows_only_integers(self):
        integer = IntegerList("5", 5, 6.7, 6, False)
        self.assertEqual(integer.get_data(), [5, 6])

        self.assertEqual(integer._IntegerList__data, [5, 6])

    def test_add_element_not_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.integerList.add("5")
        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.integerList.add(5.6)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add(self):
        self.assertEqual(self.integerList.get_data(), [4, 3, 6])

        self.integerList.add(5)
        self.assertEqual(self.integerList.get_data(), [4, 3, 6, 5])

    def test_remove_index_invalid_index_raises(self):
        self.assertEqual(self.integerList.get_data(), [4, 3, 6])

        with self.assertRaises(IndexError) as ex:
            self.integerList.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.integerList.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual(self.integerList.get_data(), [4, 3, 6])

    def test_remove_index(self):
        self.assertEqual(self.integerList.get_data(), [4, 3, 6])

        result = self.integerList.remove_index(1)

        self.assertEqual(self.integerList.get_data(), [4, 6])
        self.assertEqual(3, result)

    def test_get_index_invalid_index_raises(self):
        self.assertEqual(self.integerList.get_data(), [4, 3, 6])

        with self.assertRaises(IndexError) as ex:
            self.integerList.get(4)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.integerList.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual(self.integerList.get_data(), [4, 3, 6])

    def test_get_element_by_index(self):
        self.assertEqual(self.integerList.get_data()[0], 4)
        result = self.integerList.get(0)
        self.assertEqual(4, result)

    def test_indert_index_invalid_index_raises(self):
        self.assertEqual(self.integerList.get_data(), [4, 3, 6])

        with self.assertRaises(IndexError) as ex:
            self.integerList.insert(4, 7)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            self.integerList.insert(3, 7)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual(self.integerList.get_data(), [4, 3, 6])

    def test_insert_not_int_raises(self):
        self.assertEqual(self.integerList.get_data(), [4, 3, 6])

        with self.assertRaises(ValueError) as ex:
            self.integerList.insert(0, "7")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert(self):
        self.assertEqual(self.integerList.get_data(), [4, 3, 6])

        result = self.integerList.insert(0, 7)
        self.assertIsNone(result)

        self.assertEqual(self.integerList.get_data(), [7, 4, 3, 6])

    def test_get_biggest(self):
        integer = IntegerList(4, -3, 10, 8, -1)

        result = integer.get_biggest()

        self.assertEqual(10, result)

    def test_get_index(self):
        integer = IntegerList(4, -3, 10, 8, -1, 10)

        result = integer.get_index(10)
        self.assertEqual(2, result)




if __name__ == '__main__':
    main()