from unittest import TestCase, main

from OOP_workshop_lists.main import CustomList, BoundImpossibleError


class TestsCustomList(TestCase):
    def test_init_no_params(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__data)

    def test_init_with_params(self):
        cl = CustomList(4, "asd", 9.8)
        self.assertEqual([4, "asd", 9.8], cl._CustomList__data)

    def test_append_no_values(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__data)

        result = cl.append(5)
        self.assertEqual([5], cl._CustomList__data)
        self.assertEqual([5], result)


    def test_append_with_existing_values(self):
        cl = CustomList(4, "asd", 9.8)
        self.assertEqual([4, "asd", 9.8], cl._CustomList__data)
        result = cl.append(5)
        self.assertEqual([4, "asd", 9.8, 5], cl._CustomList__data)
        self.assertEqual([4, "asd", 9.8, 5], result)

    def test_remove_by_index(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.remove(0)
        self.assertEqual([10, 5], cl._CustomList__data)
        self.assertEqual(5, result)

    def test_remove_invalid_index(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        with self.assertRaises(IndexError) as ex:
            result = cl.remove(4)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(f"Index must be between 0 and 2", str(ex.exception))

    def test_get_index_invalid_index(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        with self.assertRaises(IndexError) as ex:
            result = cl.get(4)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(f"Index must be between 0 and 2", str(ex.exception))

    def test_get_index(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.get(0)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(5, result)

    def test_extend(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.extend([1, 2, 3])
        self.assertEqual([5, 10, 5, 1, 2, 3], cl._CustomList__data)
        self.assertEqual([5, 10, 5, 1, 2, 3], result)

    def test_extend_on_empty_list(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__data)
        result = cl.extend([1, 2, 3])
        self.assertEqual([1, 2, 3], cl._CustomList__data)
        self.assertEqual([1, 2, 3], result)

    def test_insert_invalid_index(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        with self.assertRaises(IndexError) as ex:
            cl.insert(-1, 100)

        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(f"Index must be between 0 and 2", str(ex.exception))


    def test_insert_infront(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.insert(0, 100)
        self.assertEqual([100, 5, 10, 5], cl._CustomList__data)
        self.assertEqual([100, 5, 10, 5], result)


    def test_insert_in_the_middle(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.insert(2, 100)
        self.assertEqual([5, 10, 100, 5], cl._CustomList__data)
        self.assertEqual([5, 10, 100, 5], result)

    def test_pop(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.pop()
        self.assertEqual([5, 10], cl._CustomList__data)
        self.assertEqual(5, result)

    def test_clear(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)

        result = cl.clear()
        self.assertEqual([], cl._CustomList__data)
        self.assertIsNone(result)

    def test_index_value_does_not_exist(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        result = cl.index(100)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(-1, result)

    def test_index_returns_first_occurrance(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        result = cl.index(5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(0, result)

    def test_count_no_values(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        result = cl.count(100)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(0, result)

    def test_count(self):
        cl = CustomList(5, 10, 5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        result = cl.count(5)
        self.assertEqual([5, 10, 5], cl._CustomList__data)
        self.assertEqual(2, result)

    def test_reversed(self):
        cl = CustomList(1, 10, 5)
        self.assertEqual([1, 10, 5], cl._CustomList__data)
        result = cl.reverse()

        self.assertEqual([1, 10, 5], cl._CustomList__data)
        self.assertEqual([5, 10, 1], result)

    def test_copy(self):
        cl = CustomList(1, 10, 5)
        self.assertEqual([1, 10, 5], cl._CustomList__data)

        result = cl.copy()
        self.assertEqual([1, 10, 5], cl._CustomList__data)
        self.assertEqual([1, 10, 5], result)
        self.assertNotEqual(id(cl._CustomList__data), id(result))

    def test_nested_objects_are_copied_too(self):
        cl = CustomList([1, 2], 3, 4)
        self.assertEqual([[1, 2], 3, 4], cl._CustomList__data)

        result = cl.copy()

        self.assertNotEqual(id(cl._CustomList__data), id(result))

        self.assertEqual([1,2], cl._CustomList__data[0])
        self.assertNotEqual(id(cl._CustomList__data[0]), id(result[0]))

    def test_size(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__data)

        result = cl.size()
        self.assertEqual([], cl._CustomList__data)
        self.assertEqual(0, result)

        cl.append(10)
        cl.append(20)

        result = cl.size()

        self.assertEqual([10, 20], cl._CustomList__data)
        self.assertEqual(2, result)

    def test_add_first(self):
        cl = CustomList(1, 10, 5)
        self.assertEqual([1, 10, 5], cl._CustomList__data)

        result = cl.add_first(100)
        self.assertEqual([100, 1, 10, 5], cl._CustomList__data)
        self.assertIsNone(result)

    def test_dictionaize_odd_values(self):
        cl = CustomList(1, 10, 5)
        self.assertEqual([1, 10, 5], cl._CustomList__data)

        result = cl.dictionize()
        self.assertEqual([1, 10, 5], cl._CustomList__data)
        self.assertEqual({1: 10, 5: " "}, result)

    def test_dictionaize_even_values(self):
        cl = CustomList(1, 10, 5, 6)
        self.assertEqual([1, 10, 5, 6], cl._CustomList__data)

        result = cl.dictionize()
        self.assertEqual([1, 10, 5, 6], cl._CustomList__data)
        self.assertEqual({1: 10, 5: 6}, result)

    def test_dictionaze_no_values(self):
        cl = CustomList()
        self.assertEqual([], cl._CustomList__data)
        result = cl.dictionize()
        self.assertEqual([], cl._CustomList__data)
        self.assertEqual({}, result)


    def test_move(self):
        cl = CustomList(1, 10, 5)
        self.assertEqual([1, 10, 5], cl._CustomList__data)

        result = cl.move(2)
        self.assertEqual([5, 1, 10], cl._CustomList__data)
        self.assertEqual([5, 1, 10], result)

    def test_sum(self):
        cl = CustomList(1, 10, "asd", [1, 2], 9.8)

        result = cl.sum()

        self.assertEqual(25.8, result)

    def test_sum_zero_elemetns(self):
        cl = CustomList()

        result = cl.sum()
        self.assertEqual(0, result)

    def test_overbound_with_highest_num(self):
        cl = CustomList(1, 10, "asd", [1, 2], 9.8)

        result = cl.overbound()
        self.assertEqual(1, result)

    def test_overbound_with_highest_iterable_length(self):
        cl = CustomList(1, 2, "asd", [1, 2], -3)

        result = cl.overbound()
        self.assertEqual(2, result)

    def test_no_elements_raises_overbound(self):
        cl = CustomList()

        with self.assertRaises(BoundImpossibleError) as ex:
            cl.overbound()
        self.assertEqual("No elements in the list", str(ex.exception))


    def test_underbound_with_highest_iterable_length(self):
        cl = CustomList(1, 2, "asd", [1, 2], -3)

        result = cl.underbound()
        self.assertEqual(4, result)

    def test_no_elements_raises_underbound(self):
        cl = CustomList()

        with self.assertRaises(BoundImpossibleError) as ex:
            cl.underbound()
        self.assertEqual("No elements in the list", str(ex.exception))


if __name__ == '__main__':
    main()