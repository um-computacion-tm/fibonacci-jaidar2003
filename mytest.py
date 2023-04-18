import unittest
from fibonacci1 import fibonacci
from fibonacci2 import fibonacci_iterative

class TestFibonacci(unittest.TestCase):
    def test_fibonacci1(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)

    def test_fibonacci2(self):
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(1), 1)
        self.assertEqual(fibonacci_iterative(2), 1)
        self.assertEqual(fibonacci_iterative(3), 2)
        self.assertEqual(fibonacci_iterative(4), 3)
        self.assertEqual(fibonacci_iterative(5), 5)
        self.assertEqual(fibonacci_iterative(6), 8)
        self.assertEqual(fibonacci_iterative(7), 13)
        self.assertEqual(fibonacci_iterative(8), 21)
        
if __name__ == '__main__':
    unittest.main()


