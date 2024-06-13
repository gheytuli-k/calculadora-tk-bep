import unittest
from main import add, subtract

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)  # This should pass

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 3)  # This should fail, expected 5 but incorrect logic

if __name__ == '__main__':
    unittest.main()