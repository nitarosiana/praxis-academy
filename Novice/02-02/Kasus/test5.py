import unittest
import pickle
from 5 import Animal, Sheep

class TestSort(unittest.TestCase):

    def test_animal(self):
        result = Sheep("White")
        self.assertEqual(result.color, "White")

    def test_paws(self):
        mary = Sheep("white")
        self.assertEqual(mary.number_of_paws, 4)

if __name__ == '__main__':
    unittest.main()

