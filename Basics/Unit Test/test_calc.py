import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(15,5), 20)
    
    def test_sub(self):
        self.assertEqual(calc.sub(15,5), 0)


if __name__ == '__main__':
    unittest.main()