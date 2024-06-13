import unittest
from simple import add, subtract

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5) 

if __name__ == '__main__':
    unittest.main()