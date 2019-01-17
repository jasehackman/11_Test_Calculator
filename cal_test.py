import unittest
from calculator import Calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.calc = Calculator()
    # Create an instance of the calculator that can be used in all tests

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calc.add(2, 7), 9)
    self.assertEqual(self.calc.add("a","b"), "not a number")

  def test_subtract(self):
    self.assertEqual(self.calc.subtract(7, 2), 5)
    self.assertEqual(self.calc.subtract("a","b"), "not a number")

  def test_mult(self):
    self.assertEqual(self.calc.mult(7, 2), 14)
    self.assertEqual(self.calc.mult("a","b"), "not a number")

  def test_div(self):
    self.assertEqual(self.calc.div(6, 2), 3)
    self.assertEqual(self.calc.div("a","b"), "not a number")


  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()