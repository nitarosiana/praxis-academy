import unittest
from 4 import fib,fib2

class TestFibo(unittest.TestCase):

    def test_fibo(self):
        self.assertEqual(fib2(10), [0, 1, 1, 2, 3, 5, 8])
    
if __name__ == '__main__':
    unittest.main()
