import unittest

from calculator import add, subtract, multiply, divide, calculate


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_division(self):
        self.assertEqual(divide(10, 5), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_calculate_dispatch(self):
        self.assertEqual(calculate(10, 5, "1"), 15)
        self.assertEqual(calculate(10, 5, "2"), 5)
        self.assertEqual(calculate(10, 5, "3"), 50)
        self.assertEqual(calculate(10, 5, "4"), 2)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate(10, 5, "9")


if __name__ == "__main__":
    unittest.main()
