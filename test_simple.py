import unittest
from simple import multiply

import unittest
from main import multiply

class TestMain(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)  

    def test_multiply_incorrect(self):
        self.assertEqual(multiply(3, 4), 12)  

if __name__ == '__main__':
    unittest.main()