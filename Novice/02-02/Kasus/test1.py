import unittest
from 1 import Person

class Test(unittest.TestCase):
    per = Person()

    def test_person(self):
        result = self.per.setPerson(50)
        self.assertEqual(self.per.getPerson(), 80)

if __name__ == '__main__':
    unittest.main()