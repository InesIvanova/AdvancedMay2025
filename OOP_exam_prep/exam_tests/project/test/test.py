from project.furniture import Furniture


from unittest import TestCase, main


class FurnitureTests(TestCase):
    def test_init_with_default_args(self):
        furniture = Furniture("model", 100, (1, 2, 3))
        self.assertEqual(furniture.model, "model")
        self.assertEqual(furniture.price, 100)
        self.assertEqual(furniture.dimensions, (1, 2, 3))
        self.assertTrue(furniture.in_stock)
        self.assertIsNone(furniture.weight)

    def test_init_pass_args_for_defaults(self):
        furniture = Furniture("model", 100, (1, 2, 3), False, 100)
        self.assertEqual(furniture.model, "model")
        self.assertEqual(furniture.price, 100)
        self.assertEqual(furniture.dimensions, (1, 2, 3))
        self.assertFalse(furniture.in_stock)
        self.assertEqual(furniture.weight, 100)

    def test_model_invalid_value_raises(self):
        with self.assertRaises(ValueError)as ex:
            Furniture("   ", 100, (1, 2, 3), False, 100)
        self.assertEqual(str(ex.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

        with self.assertRaises(ValueError) as ex:
            Furniture(" a "*51, 100, (1, 2, 3), False, 100)
        self.assertEqual(str(ex.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_negative_price_raises(self):
        with self.assertRaises(ValueError)as ex:
            Furniture("asd", -1, (1, 2, 3), False, 100)
        self.assertEqual(str(ex.exception), "Price must be a non-negative number.")

    def test_length_dimensions_raises(self):
        with self.assertRaises(ValueError)as ex:
            Furniture("asd", 1, (1, 2), False, 100)
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain 3 integers.")

        with self.assertRaises(ValueError) as ex:
            Furniture("asd", 1, (1, ), False, 100)
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain 3 integers.")

        with self.assertRaises(ValueError) as ex:
            Furniture("asd", 1, (), False, 100)
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain 3 integers.")

        with self.assertRaises(ValueError) as ex:
            Furniture("asd", 1, (1, 2, 3, 4), False, 100)
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain 3 integers.")

    def test_dimensions_negative_raises(self):
        with self.assertRaises(ValueError)as ex:
            Furniture("asd", 20, (1, 2, -1), False, 100)
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_negative_weight_raises(self):
        with self.assertRaises(ValueError)as ex:
            Furniture("asd", 20, (1, 2, 1), False, -1)
        self.assertEqual(str(ex.exception), "Weight must be greater than zero.")

    def test_get_available_status_in_stock(self):
        f = Furniture("asd", 20, (1, 2, 1), True, 100)
        result = f.get_available_status()
        self.assertEqual(result, f"Model: {f.model} is currently in stock.")

    def test_get_available_status_not_in_stock(self):
        f = Furniture("asd", 20, (1, 2, 1), False, 100)
        result = f.get_available_status()
        self.assertEqual(result, f"Model: {f.model} is currently unavailable.")

    def test_get_specifications_no_weight(self):
        f = Furniture("asd", 20, (1, 2, 3), False)
        result = f.get_specifications()
        self.assertEqual(result, f"Model: {f.model} has the following dimensions: 1mm x 2mm x 3mm and weighs: N/A")

    def test_get_specifications_with_weight(self):
        f = Furniture("asd", 20, (1, 2, 3), True, 100)
        result = f.get_specifications()
        self.assertEqual(result, f"Model: {f.model} has the following dimensions: 1mm x 2mm x 3mm and weighs: 100")

if __name__ == '__main__':
    main()