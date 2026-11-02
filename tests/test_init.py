import unittest

from first_init import my_func
from app import app


class MyTestCase(unittest.TestCase):
    def test_my_func(self):
        self.assertEqual(my_func(1, 2), 3)
        self.assertEqual(my_func(10, 20), 30)


if __name__ == '__main__':
    unittest.main()
