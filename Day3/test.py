import unittest
from day3 import step1, step2

class TestDay3(unittest.TestCase):
    def test(self):
        values = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
        self.assertEqual(step1(values), 198)


if __name__ == '__main__':
    unittest.main()