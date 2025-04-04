import unittest
from fibonacci import Fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_non_integer(self):
        with self.assertRaises(ValueError):
            Fibonacci("one")

    def test_fibonacci_0(self):
        self.assertEqual(list(Fibonacci(0)), [0])

    def test_fibonacci_1(self):
        self.assertEqual(list(Fibonacci(1)), [0, 1])

    def test_fibonacci_2(self):
        self.assertEqual(list(Fibonacci(2)), [0, 1, 1])

    def test_fibonacci_4(self):
        self.assertEqual(list(Fibonacci(4)), [0, 1, 1, 2, 3])

    def test_fibonacci_10(self):
        self.assertEqual(list(Fibonacci(10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fibonacci_negative(self):
        self.assertEqual(list(Fibonacci(-1)), [])

if __name__ == '__main__':
    unittest.main()
