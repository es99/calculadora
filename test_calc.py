import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calc.soma(2, 3), 5)

    def test_subtrai(self):
        self.assertEqual(calc.sub(3,2), 1)

if __name__ == '__main__':
    unittest.main()