from example_sep.project.person import Person

import unittest

class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person = Person("Luc", "Peterson", 25)

    def test_get_full_name(self):
        result = self.person.get_full_name()
        expected_result = "Luc Peterson"
        self.assertEqual(result, expected_result)

    def test_get_info(self):
        result = self.person.get_info()
        expected_result = "Luc Peterson is 25 years old"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
