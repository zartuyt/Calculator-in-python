import unittest
from CalculatorLogic import CalculatorLogic

class TestCalculatorLogic(unittest.TestCase):

    def setUp(self):
        self.calc = CalculatorLogic()

    def test_add_to_expression(self):
        self.calc.add_to_expression(5)
        self.assertEqual(self.calc.current_expression, "5")

    def test_append_operator(self):
        self.calc.add_to_expression(5)
        self.calc.append_operator("+")
        self.assertEqual(self.calc.total_expression, "5+")
        self.assertEqual(self.calc.current_expression, "")

    def test_clear(self):
        self.calc.add_to_expression(5)
        self.calc.clear()
        self.assertEqual(self.calc.current_expression, "")
        self.assertEqual(self.calc.total_expression, "")

    def test_evaluate(self):
        self.calc.add_to_expression(5)
        self.calc.append_operator("+")
        self.calc.add_to_expression(3)
        self.calc.evaluate()
        self.assertEqual(self.calc.current_expression, "8")

    def test_square(self):
        self.calc.add_to_expression(5)
        self.calc.square()
        self.assertEqual(self.calc.current_expression, "25")

    def test_sqrt(self):
        self.calc.add_to_expression(9)
        self.calc.sqrt()
        self.assertEqual(self.calc.current_expression, "3.0")

if __name__ == "__main__":
    unittest.main()
