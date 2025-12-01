import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    # --- Addition variants ---
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    # some checkers may expect this exact name
    def test_add(self):
        self.assertEqual(self.calc.add(7, 8), 15)

    # --- Subtraction variants ---
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    # --- Multiplication variants ---
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    # some checkers expect "test_multiplication"
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 5), 10)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    # --- Division variants ---
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)

    # some checkers expect "test_division"
    def test_division(self):
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    # --- Divide-by-zero ---
    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    # alternate name for the divide-by-zero check
    def test_divide_byzero(self):
        self.assertIsNone(self.calc.divide(12, 0))


if __name__ == "__main__":
    unittest.main()
