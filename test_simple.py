import unittest
from unittest.mock import patch
from simple import my_function

class TestMain(unittest.TestCase):

    def test_memory_leak(self):
        big_list = my_function()
        self.assertIsNotNone(big_list)

if __name__ == '__main__':
    unittest.main()
