import unittest
from unittest.mock import patch
from simple import generate_memory_leak

class TestMain(unittest.TestCase):

    def test_memory_leak(self):
        big_list = generate_memory_leak()
        self.assertIsNotNone(big_list)

if __name__ == '__main__':
    unittest.main()
