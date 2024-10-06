import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):    # Define what happens before any of the tests are being run
        self.calculator = Calculator ()     # initialized as a Calculator instance
    # Now we can define test cases.
    # lets think about the positives and negative cases (ex: list, string, non-val)

# ADD ADD ADD ADD ADD ADD 
    def test_add_number_returns_sum(self):
        result = self.calculator.add(x=20, y=60)
        self.assertEqual(20 + 60, result)

        result = self.calculator.add(x=20.22, y=60.89)
        self.assertEqual(20.22 + 60.89, result)

    def test_add_non_numbers_raises_type_error(self):
        self.assertRaises(TypeError, self.calculator.add, x="Hello", y="World")
        self.assertRaises(TypeError, self.calculator.add, x=20, y="World")
        self.assertRaises(TypeError, self.calculator.add, x="Hello", y=20)
        self.assertRaises(TypeError, self.calculator.add, x="128.10.10",y=20)
        self.assertRaises(TypeError, self.calculator.add, x=20, y="128.10.10")

    def test_add_string_numbers_returns_sum(self):
        result = self.calculator.add(x="50", y="20.99")
        self.assertEqual(50 + 20.99, result)

        result = self.calculator.add(x=50, y="20.99")
        self.assertEqual(50 + 20.99, result)

        result = self.calculator.add(x="50", y=20.99)
        self.assertEqual(50 + 20.99, result)

# SUBTRACT SUBTRACT SUBTRACT SUBTRACT SUBTRACT 
    def test_subtract_number_returns_subtract(self):
        result = self.calculator.subtract(x=20, y=60)
        self.assertEqual(20 - 60, result)

        result = self.calculator.subtract(x=20.22, y=60.89)
        self.assertEqual(20.22 - 60.89, result)

    def test_subtract_non_numbers_raises_type_error(self):
        self.assertRaises(TypeError, self.calculator.subtract, x="Hello", y="World")
        self.assertRaises(TypeError, self.calculator.subtract, x=20, y="World")
        self.assertRaises(TypeError, self.calculator.subtract, x="Hello", y=20)
        self.assertRaises(TypeError, self.calculator.subtract, x="128.10.10",y=20)
        self.assertRaises(TypeError, self.calculator.subtract, x=20, y="128.10.10")

    def test_subtract_string_numbers_returns_subtract(self):
        # Test with string inputs
        result = self.calculator.subtract(x="50", y="20.99")
        self.assertEqual(50 - 20.99, result)

        result = self.calculator.subtract(x="20.99", y="50")
        self.assertEqual(20.99 - 50, result)

        result = self.calculator.subtract(x=50, y="20.99")
        self.assertEqual(50 - 20.99, result)

        result = self.calculator.subtract(x="50", y=20.99)
        self.assertEqual(50 - 20.99, result)

        # Test with negative string inputs
        result = self.calculator.subtract(x="-50", y="20.99")
        self.assertEqual(-50 - 20.99, result)

        result = self.calculator.subtract(x="20.99", y="-50")
        self.assertEqual(20.99 - (-50), result)

        result = self.calculator.subtract(x="-50", y="-20.99")
        self.assertEqual(-50 - (-20.99), result)

# MULTIPLICATION MULTIPLICATION MULTIPLICATION 
    def test_multiply_string_numbers_returns_product(self):
        result = self.calculator.multiply(x="5", y="6")
        self.assertEqual(5 * 6, result)

        result = self.calculator.multiply(x="3.5", y="2")
        self.assertEqual(3.5 * 2, result)

        result = self.calculator.multiply(x=4, y="2.5")
        self.assertEqual(4 * 2.5, result)

        result = self.calculator.multiply(x="-3", y="3")
        self.assertEqual(-3 * 3, result)

        result = self.calculator.multiply(x="3", y="-3")
        self.assertEqual(3 * -3, result)

    def test_invalid_inputs_multiply_raise_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.multiply(x="Hello", y="World")

        with self.assertRaises(TypeError):
            self.calculator.multiply(x=20, y="World")

        with self.assertRaises(TypeError):
            self.calculator.multiply(x="Hello", y=20)

# DIVISION DIVISION DIVISION DIVISION DIVISION 
    def test_divide_string_numbers_returns_quotient(self):
        result = self.calculator.divide(x="12", y="4")
        self.assertEqual(12 / 4, result)

        result = self.calculator.divide(x="7.5", y="2.5")
        self.assertEqual(7.5 / 2.5, result)

        result = self.calculator.divide(x=10, y="5")
        self.assertEqual(10 / 5, result)

        result = self.calculator.divide(x="-10", y="2")
        self.assertEqual(-10 / 2, result)

        result = self.calculator.divide(x="9", y="-3")
        self.assertEqual(9 / -3, result)

    def test_invalid_inputs_divide_raise_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.divide(x="Hello", y="World")

        with self.assertRaises(TypeError):
            self.calculator.divide(x=20, y="World")

        with self.assertRaises(TypeError):
            self.calculator.divide(x="Hello", y=20)

        # Test division by zero
        with self.assertRaises(ValueError):
            self.calculator.divide(x=10, y=0)

if __name__ == '__main__':
    unittest.main()