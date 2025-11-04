from unittest import TestCase
from test_lecture import calculate_average

class Test(TestCase):
    def test_calculate_average(self):
        self.assertEqual(calculate_average([3, 3, 3]), 3)
