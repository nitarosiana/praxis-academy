import unittest
from 3 import bubble_sort

class TestSort(unittest.TestCase):

    def test_sort(self):
        lst = [4,3,5,1,2]
        self.assertEqual(bubble_sort(lst), lst.sort())
    
if __name__ == '__main__':
    unittest.main()
